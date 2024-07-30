import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img, img_to_array


#GRAFICO ALGUNAS IMÁGENES PARA VER EL FUNCIONAMIENTO DEL MODELO
def testing_model(model):
    datagen_testing = ImageDataGenerator(rescale=1./255)

    data_testing = datagen_testing.flow_from_directory(
        "testing_dataset",
        target_size=(224,224),
        color_mode = "rgb",
        shuffle= True
    )

    clases_names=["no", "yes"]

    # Obtengo las imagenes y sus etiquetas
    images_testing, labels_testing = next(data_testing)
    predictions = model.predict(images_testing)

    labels_testing = np.argmax(labels_testing, axis=1)

    rows = 5
    columns = 4
    num_images = rows * columns
    plt.figure(figsize=(2*2*columns, 2*rows))
    for i in range(num_images):
        plt.subplot(rows, 2*columns, 2*i+1)
        plot_image(i, predictions, labels_testing, images_testing, clases_names)
        plt.subplot(rows, 2*columns, 2*i+2)
        plot_value(i, predictions, labels_testing)

    plt.tight_layout()
    plt.show()


  
def plot_image(i, arr_predictions, labels_true, images, clases_names):
    arr_predictions, label_true, img = arr_predictions[i], labels_true[i], images[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img[..., 0], cmap=plt.cm.binary)
    
    label_prediction = np.argmax(arr_predictions)
    if label_prediction == label_true:
        color = 'blue'
    else:
        color = 'red'
    
    plt.xlabel("{} {:2.0f}% ({})".format(clases_names[label_prediction],
                                         100*np.max(arr_predictions),
                                         clases_names[label_true]),
               color=color)

def plot_value(i, arr_predictions, label_real):
    arr_predictions, label_real = arr_predictions[i], label_real[i]
    plt.grid(False)
    plt.xticks(range(2))
    plt.yticks([])
    grafica = plt.bar(range(2), arr_predictions, color="#777777")
    plt.ylim([0, 1]) 
    label_prediction = np.argmax(arr_predictions)
    
    grafica[label_prediction].set_color('red')
    grafica[label_real].set_color('blue')


def predict_and_save(image_path, model, output_path="output.jpg"):
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