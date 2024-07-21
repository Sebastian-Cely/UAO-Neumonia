import unittest
import os
from read_img import read_dicom_file, read_jpg_file

class TestReadImg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = os.path.dirname(__file__)
        cls.dicom_path = os.path.join(cls.test_dir, 'test_img', 'normal (2).dcm')
        cls.jpg_path = os.path.join(cls.test_dir, 'test_img', 'NORMAL2-IM-1145-0001.jpeg')

    def test_read_dicom_file(self):
        img_array, img2show = read_dicom_file(self.dicom_path)
        self.assertEqual(img_array.shape[2], 3)

    def test_read_jpg_file(self):
        img_array, img2show = read_jpg_file(self.jpg_path)
        self.assertEqual(img_array.shape[2], 3)

if __name__ == '__main__':
    unittest.main()
