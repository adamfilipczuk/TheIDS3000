# Tensorflow Model Training Instructions
The Tensorflow model is trained on `conn.log.labeled` csv data from the IoT-23 dataset. The default model distributed with the project is trained on `CTU-Honeypot-Capture-4-1` (Phillips Hue), `CTU-Honeypot-Capture-5-1` (Amazon Alexa), `CTU-IoT-Malware-Capture-3-1` (Muhstik), and `CTU-IoT-Malware-Capture-34-1` (Mirai).

Use a `conn.log.labeled` file as your base. You may add more data to the file if you would like to train on multiple dataset objects, just copy the data from the file, leaving the headers behind and paste at the bottom of your base `conn.log.labeled` file. Check the headers to make sure all headers are tab-delineated. If the headers are delineated by spaces '   ' instead of tabs '    ', delete the spaces and replace with a single tab. You may then save this file to `./src/ids3000/tools/classifier/data/conn.log.labeled`.

Navigate to `./src/ids3000/tools/classifier/`, and run the training file with `python training.py` or `python3 training.py` depending on your operating system.

## Tips
- Training will take some time, especially if training on a laptop.
- If you experience errors due to memory allocation you may need to run the training file on a device with more RAM.
