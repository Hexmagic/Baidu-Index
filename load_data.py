import numpy as np
import pathlib
from PIL import Image, ImageOps


def load_data(folder, target_index=2):
    datas = []
    targets = []
    for image_file in pathlib.Path(folder).iterdir():
        split = image_file.stem.split('_')
        target = split[target_index]
        if target == ',':
            target = 10
        else:
            target = int(target)
        image = Image.open(str(image_file.absolute()))
        image = ImageOps.invert(image)
        image_arr = np.array(image)
        image_arr[image_arr < 200] = 0
        image_arr[image_arr > 200] = 255

        try:
            datas.append(image_arr.reshape(14, 10, 1))
        except Exception:
            zeros = np.zeros((14, 10))
            zeros[:, :image_arr.shape[1]] += image_arr
            datas.append(zeros.reshape(14, 10, 1))
        targets.append(target)
    return datas, np.array(targets)