
# (⊙﹏⊙)
今天才发现百度良心发现，指数直接给出了数字，不需要再识别了,新的百度指数代码 https://github.com/Hexmagic/BaiduIndexNew.git

# 优点
精准的百度指数抓取,综合已有百度指数爬虫优点，做到精准易用

# 使用方法
首先要安装依赖包
```
pip install -r requirement.txt
```
**注意**：    
* selenium的chromeDriver需要自行下载对应版本，
* lxml包需要vsbuild tool,可以在csdn找到或者到我的博客留言发给你
* tensorflow 最新支持3.6,所以最好使用python3.6


安装好依赖包,就可以开始抓取了
抓取之前首先要登录，执行登录命令，保存为本地cookie文件以备后续测试使用，有了登录文件便可以直接使用脚本进行抓取关键词了

# 模型数据生成
模型使用tensorflow作为后端进行训练，这里简单说下怎么生成训练和测试样本,切换到model目录,运行下面的脚本
```
python generate_date.py

```
根据提示生成测试和训练脚本，生成的数据分别位于test和train目录
> 确保该目录在生成之前不存在
# 训练模型
生成好训练和测试数据直接运行下面的命令
```
python train_model.py
```
该命令生成了一个序列化的模型，名字为model.h5(代码自带一个训练好的model)

模型准确的截图，使用了增强后的数据训练的，精确度达到97%，对于百度的原始图片估计可以做到99%的精准度

![训练结果](/screenshoot.png)
