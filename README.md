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

# 流程
具体流程参考我的简书博文 ![百度指数抓取 selenium 💗 Keras](https://www.jianshu.com/p/5f29bc4552e4)
