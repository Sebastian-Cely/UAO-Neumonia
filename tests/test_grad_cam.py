import unittest
import numpy as np
from grad_cam import grad_cam

class TestGradCam(unittest.TestCase):
    
    def test_grad_cam(self):
        array = np.random.randint(0, 256, (512, 512, 3), dtype=np.uint8)
        heatmap = grad_cam(array)
        self.assertEqual(heatmap.shape, (512, 512, 3))
        
if __name__ == '__main__':
    unittest.main()