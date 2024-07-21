import unittest
import numpy as np
from integrator import predict


class TestIntegrator(unittest.TestCase):

    def test_predict(self):
        array = np.random.randint(0, 256, (512, 512, 3), dtype=np.uint8)
        label, proba, heatmap = predict(array)
        self.assertIn(label, ["bacteriana", "normal", "viral"])
        self.assertIsInstance(proba, float)
        self.assertEqual(heatmap.shape, (512, 512, 3))


if __name__ == "__main__":
    unittest.main() 
