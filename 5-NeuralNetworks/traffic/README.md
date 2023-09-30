 # Traffic Sign Recognition AI

An AI model designed to identify which traffic sign appears in a given photograph.

## Usage
Download the dataset https://cdn.cs50.net/ai/2023/x/projects/5/gtsrb.zip for this project and unzip it. Move the resulting gtsrb directory inside of your traffic directory.

Install dependencies:
```bash
pip3 install -r requirements.txt
```
To train the AI and test its accuracy:
```bash
python3 traffic.py gtsrb
```

## Sample Output

On executing the above command, the AI will train on the provided dataset and display its progress:
Epoch 1/10
500/500 [==============================] - 5s 9ms/step - loss: 3.7139 - accuracy: 0.1545
...
Epoch 10/10
500/500 [==============================] - 10s 20ms/step - loss: 0.2497 - accuracy: 0.9256
333/333 - 5s - loss: 0.1616 - accuracy: 0.9535

## Background

As autonomous vehicles continue to evolve, one of the critical challenges is computer vision, allowing these vehicles to understand their environment through digital imagery. Specifically, this involves the capability to recognize and distinguish various road signs. This project aims to use TensorFlow to construct a neural network that can classify road signs based on images.

For training and testing purposes, the German Traffic Sign Recognition Benchmark (GTSRB) dataset is employed. This dataset comprises thousands of images representing 43 different types of road signs.

## Key Features

- **Dataset Processing**: Uses the OpenCV-Python (cv2) module to process each image into a numpy.ndarray. Each image is resized to a consistent size, ensuring it's suitable for neural network input.

- **Neural Network**: Constructs and trains a neural network using TensorFlow. The design of the network, including the number of layers, types of layers, and additional parameters, is optimized for traffic sign classification.

## Experimentation