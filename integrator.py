import numpy as np
from preprocess_img import preprocess
from grad_cam import grad_cam
from load_model import load_model

# Método de predicción mediante carga del modelo
def predict(array):
    # 1. Llamado de la función para pre-procesar la imagen a un formato de lotes 
    batch_array_img = preprocess(array)
    # 2. Llamar la función para cargar el modelo que predice la clase y la probabilidad. 
    #model_cnn = load_model('../conv_MLP_84.h5')
    model_cnn = load_model('conv_MLP_84.h5')
    prediction = np.argmax(model_cnn.predict(batch_array_img))
    proba = np.max(model_cnn.predict(batch_array_img)) * 100
    label = ""
    if prediction == 0:
        label = "bacteriana"
    elif prediction == 1:
        label = "normal"
    elif prediction == 2:
        label = "viral"
    # 3. Llama la función para generar el Grad_CAM: devuelve una imagen con el mapa de calor superpuesto
    heatmap = grad_cam(array)
    return (label, proba, heatmap) 