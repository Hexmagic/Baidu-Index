import Augmentor
import shutil

pipe = Augmentor.Pipeline('source')
# 2. 增强操作
# 旋转 概率0.7，向左最大旋转角度10，向右最大旋转角度10
pipe.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
# 放大 概率0.3，最小为1.1倍，最大为1.6倍；1不做变换
pipe.zoom(probability=0.3, min_factor=1.1, max_factor=1.6)
# resize 同一尺寸 200 x 200
# p.resize(probability=1,height=200,width=200) 这段我没用
# 3. 指定增强后图片数目总量
index = int(input('\n生成数据：1 训练数据 2 测试数据:\t'))
number = int(input('输入样本数量:\t'))
pipe.sample(number)
shutil.move('source/output', 'train' if index == 1 else 'test')
