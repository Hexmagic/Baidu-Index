import numpy as np
from keras.layers import (Conv2D, Dense, Dropout, Flatten, MaxPooling2D)
from keras.models import Sequential
from keras.optimizers import Adadelta
from keras.utils import to_categorical
from sklearn.utils import shuffle
import pathlib
from PIL import Image, ImageOps


def load_data(folder, target_index=2):
    datas = []
    targets = []
    for image_file in pathlib.Path(folder).iterdir():
        split = image_file.stem.split('_')
        target = split[target_index]
        if target == ',':
            target = 10  #这里我偷懒用10代表','#
        else:
            target = int(target)
        image = Image.open(str(image_file.absolute()))
        image = image.convert('L')
        image = ImageOps.invert(image)  # 原来的图片是黑色背景需要反转
        image_arr = np.array(image)
        image_arr[image_arr < 200] = 0  # 极值化处理，去除噪音点
        image_arr[image_arr > 200] = 255
        datas.append(image_arr.reshape(14, 8, 1))
        targets.append(target)
    return np.array(datas), np.array(targets)


x_train, y_train = load_data("train")
x_test, y_test = load_data("test")
x_train = np.array(x_train)
x_test = np.array(x_test)
x_train, y_train = shuffle(x_train, y_train)
y_train = to_categorical(y_train, num_classes=11)
x_test, y_test = shuffle(x_test, y_test)
y_test = to_categorical(y_test, num_classes=11)

model = Sequential()
model.add(Conv2D(32, (2, 2), input_shape=(14, 8, 1), activation='relu'))
model.add(Conv2D(32, (2, 2), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (2, 2), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dropout(0.15))
model.add(Dense(128, activation='relu'))
model.add(Dense(11, activation='softmax'))
model.compile(
    loss='categorical_crossentropy',
    optimizer=Adadelta(lr=1, decay=0.05),
    metrics=['accuracy'])
model.fit(x_train, y_train, epochs=30, batch_size=300)
score = model.evaluate(x_test, y_test, batch_size=200)
print(score)
model.save('model.h5')