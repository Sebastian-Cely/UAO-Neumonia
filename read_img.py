import os
import cv2
import pydicom
from PIL import Image
import numpy as np

<<<<<<< HEAD
# Método de lectura de imágenes en formato DICOM
=======
>>>>>>> 166ab163301804f0ebc32383dc0bf426f32ef836
def read_dicom_file(path):
    img = pydicom.read_file(path)
    img_array = img.pixel_array
    img2show = Image.fromarray(img_array)
    img2 = img_array.astype(float)
    img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
    img2 = np.uint8(img2)
    img_RGB = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
    return img_RGB, img2show

<<<<<<< HEAD
# Método de lectura de imágenes JPEG
=======
>>>>>>> 166ab163301804f0ebc32383dc0bf426f32ef836
def read_jpg_file(path):
    path = os.path.normpath(path)
    img = cv2.imread(path)
    img_array = np.asarray(img)
    img2show = Image.fromarray(img_array)
    img2 = img_array.astype(float)
    img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
    img2 = np.uint8(img2)
    return img2, img2show
