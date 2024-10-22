
# Flower Classification using Transfer Learning with MobileNetV2

This project demonstrates the use of transfer learning to classify flower images into five categories: `daisy`, `dandelion`, `roses`, `sunflowers`, and `tulips`. The model is built using TensorFlow and employs a pre-trained `MobileNetV2` model to extract features, which are then fine-tuned for the classification task. The dataset is sourced from [TensorFlow Flower Photos](https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz).

## Table of Contents

- [Project Overview](#project-overview)
- [Setup](#setup)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Fine-Tuning](#fine-tuning)
- [Evaluation](#evaluation)
- [Predictions](#predictions)
- [Model Export](#model-export)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project uses transfer learning to build a flower image classifier. By leveraging the power of the pre-trained `MobileNetV2` model, we can classify flower images efficiently. The key steps include:

1. Loading and preprocessing the flower dataset.
2. Building the classification model using `MobileNetV2`.
3. Training the model on the dataset with data augmentation.
4. Fine-tuning the top layers of the pre-trained model.
5. Evaluating the model and visualizing results.
6. Exporting the trained model for TensorFlow Lite deployment.

## Setup

### Requirements

- Python 3.x
- TensorFlow 2.x
- Matplotlib
- NumPy
- OpenCV (for additional image processing)
- Google Colab (optional for training on GPU)

Install the required packages using:

```bash
pip install tensorflow numpy matplotlib opencv-python
```

### Running the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/flower-classification.git
   cd flower-classification
   ```

2. Download the dataset and extract it:
   ```bash
   wget https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz
   tar -xzvf flower_photos.tgz
   ```

3. Run the training script:
   ```bash
   python train.py
   ```

## Dataset

The dataset consists of 5 classes of flower images:
- Daisy
- Dandelion
- Roses
- Sunflowers
- Tulips

You can download the dataset from [here](https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz).

## Model Architecture

The model is built using a pre-trained `MobileNetV2` model as the base for feature extraction, followed by fully connected layers for classification:

```python
model = tf.keras.Sequential([
    pretrained_model,
    tf.keras.layers.Flatten(input_shape=(192, 192)),
    tf.keras.layers.Dense(120, activation='relu'),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Dense(20, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(5, activation='softmax')
])
```

- **Pretrained Model:** MobileNetV2 is used without the top layers.
- **Dropout Layers:** Prevent overfitting by randomly dropping 20% and 40% of the units.
- **Dense Layers:** Fully connected layers for the final classification task.

## Training

The model is trained with the following configuration:
- **Batch Size:** 64
- **Epochs:** 40
- **Optimizer:** Adam with a learning rate of `0.00001`
- **Loss Function:** Sparse Categorical Crossentropy
- **Metrics:** Accuracy

Data augmentation techniques such as random flipping and rotation are applied to enhance the training dataset.

### Command to train:
```python
history = model.fit(augmented_train_dataset, steps_per_epoch=steps_per_epoch, epochs=40,
                    validation_data=validation_dataset, validation_steps=validation_steps)
```

## Fine-Tuning

After initial training, fine-tuning is performed on the top layers of the `MobileNetV2` model to adapt the generic features to our specific dataset:

```python
pretrained_model.trainable = True
for layer in pretrained_model.layers[:100]:
    layer.trainable = False  # Freeze all layers before the 100th layer
```

## Evaluation

The model's performance is evaluated using the validation dataset. The accuracy and loss over training epochs can be visualized using:

```python
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()
```

## Predictions

You can make predictions on new images using the trained model:

```python
predictions = model.predict(image)
predicted_class = CLASSES[np.argmax(predictions)]
```

Sample images and predictions are displayed using Matplotlib:

```python
display_9_images_with_predictions(flowers, predictions, labels)
```

## Model Export

For deployment purposes, the trained model can be exported to TensorFlow Lite:

```bash
model.save("models/flower_classifier.h5")
```

