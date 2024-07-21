import unittest
import numpy as np
from preprocess_img import preprocess

class TestPreprocess(unittest.TestCase):
    def test_preprocess(self):
        array = np.random.randint(0, 256, (512, 512, 3), dtype=np.uint8)
        processed_array = preprocess(array)
        
        self.assertEqual(processed_array.shape, (1, 512, 512, 1))
        self.assertTrue(np.all(processed_array >= 0) and np.all(processed_array <= 1))

if __name__ == '__main__':
    unittest.main()