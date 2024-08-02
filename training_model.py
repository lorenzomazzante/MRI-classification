import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tf_keras as tfk
import os
from sklearn.model_selection import train_test_split

directory = "brain_tumor_dataset"

images = []
labels = []

# Recorro el directorio y leo las imágenes
for category in os.listdir(directory):
    rute_category = os.path.join(directory, category)
    for image_name in os.listdir(rute_category):
        image_rute = os.path.join(rute_category, image_name)
        # Leo la imagen
        image = tf.keras.preprocessing.image.load_img(image_rute, target_size=(224,224))
        image_array = tf.keras.preprocessing.image.img_to_array(image) / 255.0  # Normalizo la imagen
        images.append(image_array)
        # Asigno la etiqueta (0 para "no" y 1 para "yes")
        labels.append(1 if category == "yes" else 0)

# Convierto las listas en matrices numpy
images = np.array(images)
labels = np.array(labels)

# Divido los datos en conjuntos de entrenamiento y validación
X_training, X_testing, y_training, y_testing = train_test_split(images, labels, test_size=0.3, random_state=42)

url = "https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/5"

movilenetv2 = hub.KerasLayer(url, input_shape=(224,224,3), trainable=False)

model = tfk.Sequential([
    movilenetv2,
    tfk.layers.Dense(2,activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics = ["accuracy"]
)
training = model.fit(
    X_training,
    y_training,
    epochs=1,
    validation_data = (X_testing, y_testing)
)

model.save("my_model.h5")