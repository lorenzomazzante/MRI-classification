import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator






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


