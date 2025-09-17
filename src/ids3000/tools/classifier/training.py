import pathlib
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

#
#
# This script trains a tensorflow model to classify eve.json logs to 
# provide a likelyhood of maliciousness based on previous training data. 
#
# To run training, ensure there is a file inside ./data called conn.log.labeled and that tensorflow + numpy are installed. 
#
#This model was trained using 
# CTU-IoT-Malware-Capture-34-1 
# CTU-IoT-Malware-Capture-3-1
#

LEARNING_DATA_PATH = pathlib.Path("./data/conn.log.labeled")
BATCH_SIZE = 8192
EPOCHS = 20
RANDOM_STATE = 42
TEST_SIZE = 0.20
LEARN_RATE = 1e-3
DROPOUT = 0.3
HIDDEN_UNITS = [256, 128, 64]

# IMPORT TRAINING DATA

df = pd.read_csv(LEARNING_DATA_PATH, sep="\t", comment="#", low_memory=False)

# SORT+CLEAN TRAINING DATAFRAME

df.columns = df.columns.str.strip()

    # convert benign/malicious labels to 0 and 1 respecively

label_map = {"Benign": 0, "Malicious": 1}

df["label"] = df["label"].map(label_map).astype(int)

    # Import numeric columns and convert non numeric entries to 0
NUMERIC_COLUMNS = [
    "id.orig_p", "id.resp_p", "orig_pkts", "resp_pkts", "orig_ip_bytes", "resp_ip_bytes"
]

for column in NUMERIC_COLUMNS:
    df[column] = pd.to_numeric(df[column], errors="coerce").fillna(0)


OTHER_COLUMNS = ["proto", "service", "id.resp_h", "id.orig_h"]

# Add columns available in training data and eve.json together and set dataframe for training. 

TRAINING_COLUMNS = (NUMERIC_COLUMNS+OTHER_COLUMNS)
print(TRAINING_COLUMNS)

X = df[TRAINING_COLUMNS]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE,
    stratify=y,
)


# PREPROCESSING 
numeric_features = NUMERIC_COLUMNS 

normalizer = {}
for name in numeric_features:
    norm = layers.Normalization()
    norm.adapt(np.array(X_train[name]).reshape(-1, 1))
    normalizer[name] = norm


categorical_features = ["id.orig_h", "id.resp_h", "proto", "service"]
cat_lookup = {}
cat_onehot = {}
for name in categorical_features:
    lookup = layers.StringLookup(output_mode="int", mask_token=None)
    lookup.adapt(X_train[name].fillna("___MISSING___"))
    cat_lookup[name] = lookup

    onehot = layers.CategoryEncoding(
        num_tokens=lookup.vocabulary_size(),
        output_mode="binary",
    )
    cat_onehot[name] = onehot

#

def make_preprocessor() -> tf.keras.Model:
    # numeric inputs 
    num_in = {
        n: tf.keras.Input(shape=(1,), name=n, dtype=tf.float32)
        for n in numeric_features
    }
    num_out = [normalizer[n](num_in[n]) for n in numeric_features]


    # categorical inputs 
    cat_in = {
        n: tf.keras.Input(shape=(1,), name=n, dtype=tf.string)
        for n in categorical_features
    }
    cat_out = [
        cat_onehot[n](cat_lookup[n](cat_in[n]))
        for n in categorical_features
    ]

    # concatenate 
    concatenated = tf.keras.layers.Concatenate()(
        num_out + cat_out
    )

    return tf.keras.Model(
        inputs={**num_in, **cat_in},
        outputs=concatenated,
        name="preprocessor",
    )


preprocessor = make_preprocessor()


def build_classifier(input_dim: int,
                    hidden_units: list[int] = HIDDEN_UNITS,
                    dropout: float = DROPOUT) -> tf.keras.Model:
    inputs = tf.keras.Input(shape=(input_dim,), name="features")

    x = inputs

    for units in hidden_units:
        x = tf.keras.layers.Dense(units, activation="relu")(x)
        x = tf.keras.layers.Dropout(dropout)(x)
    
    logits = tf.keras.layers.Dense(1, name="logits")(x)
    prob   = tf.keras.layers.Activation("sigmoid", name="prob")(logits)

    return tf.keras.Model(inputs, prob, name="suricata_flow_classifier")


classifier = build_classifier(preprocessor.output_shape[1])
classifier.summary()


def df_to_dataset(df_: pd.DataFrame,
                  label_: pd.Series,
                  shuffle: bool = True,
                  batch_size: int = BATCH_SIZE) -> tf.data.Dataset:
    ds = tf.data.Dataset.from_tensor_slices((dict(df_), label_.values))

    if shuffle:
        ds = ds.shuffle(buffer_size=len(df_), seed=RANDOM_STATE,
                        reshuffle_each_iteration=True)
    
    return ds.batch(batch_size).prefetch(tf.data.AUTOTUNE)


train_ds = df_to_dataset(X_train, y_train, shuffle=True)
val_ds   = df_to_dataset(X_test,  y_test,  shuffle=False)

def map_preprocess(features, label):
    """Run the Keras preprocessor and cast label to float."""
    return preprocessor(features), tf.cast(label, tf.float32)


train_prepared = train_ds.map(map_preprocess)
val_prepared   = val_ds.map(map_preprocess)

pos_weight = (y_train == 0).sum() / (y_train == 1).sum()
print(f" Positive‑class weight = {pos_weight:.3f}")

classifier.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=LEARN_RATE),
    loss=tf.keras.losses.BinaryCrossentropy(),
    metrics=[
        tf.keras.metrics.AUC(name="auc"),
        tf.keras.metrics.Precision(name="precision"),
        tf.keras.metrics.Recall(name="recall"),
    ],
)

#Start Training
history = classifier.fit(
    train_prepared,
    epochs=EPOCHS,
    validation_data=val_prepared,
    class_weight={0: 1.0, 1: pos_weight},
    verbose=2,
)

print("\nTraining finished.\n")


model_dir = pathlib.Path("./saved_model")
model_dir.mkdir(parents=True, exist_ok=True)

preprocessor.save("./saved_model/preprocessor_tf_min.keras")
classifier.save("./saved_model/classifier_tf_min.keras")


print("\nSaved Model.\n")

