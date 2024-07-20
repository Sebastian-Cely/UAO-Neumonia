import tensorflow as tf
import os

def load_model(model_path):
    return tf.keras.models.load_model(model_path)
    
