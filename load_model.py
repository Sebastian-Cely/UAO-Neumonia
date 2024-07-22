import tensorflow as tf
import os

# Método de carga del modelo de ML
def load_model(model_path):
    return tf.keras.models.load_model(model_path)