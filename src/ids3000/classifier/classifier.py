import pathlib
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
import json

#
#
# This file loads the classifier model trained on 
# CTU-IoT-Malware-Capture-34-1 
# CTU-IoT-Malware-Capture-3-1
#
# The script loads the trained model, inputs the relevant data 
# then returns a probability of traffic being malicious.
#
#

# 1. TO DO Update to include windows
model_dir = pathlib.Path("./saved_model")

preprocessor = tf.keras.models.load_model(
    model_dir / "preprocessor_tf_min.keras")

classifier = tf.keras.models.load_model(model_dir / "classifier_tf_min.keras")


input_names = [tensor.name.split(":")[0] for tensor in preprocessor.inputs]
input_map   = dict(zip(input_names, preprocessor.inputs))

numeric_features = [n for n, t in input_map.items() if t.dtype == tf.float32]
string_features  = [n for n, t in input_map.items() if t.dtype == tf.string]

print("\n Model expects the following feature groups \n")
print(f"numeric ({len(numeric_features)}): {numeric_features[:5]}")
print(f"string  ({len(string_features)}): {string_features[:5]}\n")


def make_tf_feature_dict(raw_dict: dict) -> dict:
    """Convert raw python values → tf.Tensors of shape (1,) with the correct dtype."""
    tf_dict = {}
    # numeric dictionary
    for name in numeric_features:
        value = raw_dict.get(name, 0.0)
        tf_dict[name] = tf.convert_to_tensor([value], dtype=tf.float32)

    # string dictionary
    for name in string_features:
        value = raw_dict.get(name, "___MISSING___")
        tf_dict[name] = tf.convert_to_tensor([str(value)], dtype=tf.string)

    return tf_dict


def run_prob(features_tf):
    dense_vec   = preprocessor(features_tf)
    prob_tensor = classifier(dense_vec)

    probability = prob_tensor.numpy().item()
    threshold   = 0.5
    pred_label  = int(probability >= threshold)

    print(f"Malicious probability = {probability:.4f}")
    print(f"Predicted label       = {pred_label} (0 = benign, 1 = malicious)\n\n")


# 2. Allow input from crewAI or pre crewai running. 

f = open("./data/eve.json", "r")
# def classify_eve(data):
#     classified_data = []

for a in range(0,5):
    obj=json.loads(f.readline())
    # print(obj['event_type'])
    
    if(obj.get('event_type')!="stats"):
        flow = obj.get("flow")
        service = obj.get("metadata", {}).get("flowbits")

        flow_dict = {}
        if service is not None and "http.dottedquadhost" in service:
            service = "http"
        elif service is not None and "is_proto_irc" in service:
            service = 'irc'
        else:
            service = '-'
        
        if(flow):
            #print(flow)
            flow_dict = {
                'id.orig_p': int(flow.get("src_port") or 0), 
                'id.resp_p': int(flow.get("dest_port") or 0), 
                'orig_pkts': int(flow.get("pkts_toserver") or 0), 
                'resp_pkts': int(flow.get("pkts_toclient") or 0), 
                'orig_ip_bytes': int(flow.get("bytes_toserver") or 0), 
                'resp_ip_bytes': int(flow.get("bytes_toclient") or 0), 
                'proto': str(obj.get("proto").lower()), 
                'service': str(service), 
                'id.resp_h': str(flow.get("dest_ip")), 
                'id.orig_h': str(flow.get("src_ip"))
                }
            if flow_dict.get("id.orig_p") != None:
                print(flow_dict)
                tf_dict = make_tf_feature_dict(flow_dict)
                run_prob(tf_dict)
    else:
        print(f"\nIncompatible for classification:\n {a}")

    

    # return classified_data