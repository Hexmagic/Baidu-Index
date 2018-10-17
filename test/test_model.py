import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps
import unittest
from pathlib import Path


class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = load_model('model/model.h5')
        self.test_dir = Path('btc_images')

    def test_model(self):
        for image in self.test_dir.iterdir():
            x = self.load(image.absolute())
            y = self.model.predict(x)
            y = y.argsort()[:, -1]
            y = ''.join(list(map(lambda x: ',' if x == 10 else str(x), y)))
            print('iamge_name:{}    rst: {}'.format(image, y))

    def load(self, filename):
        x = []
        image = Image.open(filename)
        image = ImageOps.invert(image)
        arr = np.array(image)
        datas = np.hsplit(arr, 5)
        for ele in datas:
            zeros = np.zeros((14, 10))
            zeros[:, :ele.shape[1]] += ele
            x.append(zeros.reshape(14, 10, 1))
        return np.array(x)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
