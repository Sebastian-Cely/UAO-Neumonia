import unittest
import os
from tensorflow.keras.models import Model
from load_model import load_model

class TestLoadModel(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.test_dir = os.path. dirname(__file__)
        cls.model_path = os.path.join(cls.test_dir, '../../', 'conv_MLP_84.h5')
        
    def test_load_model(self): 
        model = load_model(self.model_path)
        self.assertIsInstance(model, Model)
        
if __name__ == '__main__':
    unittest.main()