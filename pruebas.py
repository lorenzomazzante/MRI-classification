import numpy as np
import matplotlib.pyplot as plt
import tensorflow_hub as hub
import tensorflow as tf
import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model



image_path = "C:/Users/Mariano/Documents/Lorenzo/Boludines/MRI - clasification/aplication/image_to_analyze.jpg"
output_path = "C:/Users/Mariano/Documents/Lorenzo/Boludines/MRI - clasification/aplication/output.jpg"

model = keras.models.load_model("my_model.h5", custom_objects = {"KerasLayer": hub.KerasLayer})

# Cargar y preprocesar la imagen
img = load_img(image_path, target_size=(224, 224))
img_array = img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)  # Expandir dimensiones para que coincidan con la entrada del modelo

# Hacer la predicción
predictions = model.predict(img_array)
probability_no, probability_yes = predictions[0]

# Mostrar la imagen con la predicción
plt.figure(figsize=(6, 6))
plt.imshow(img)
plt.title(f"Probability of No Tumor: {probability_no:.2f}, Probability of Tumor: {probability_yes:.2f}")
plt.axis('off')
    
# Guardar la imagen con la predicción
plt.savefig(output_path)
plt.show()