from channel.baidu import Baidu
import os

bd = Baidu()
if not os.path.exists('baidu.cookie'):
    print("第一次需要登录\n")
    username = input("username: ")
    password = input("password: ")
    bd.login(username, password)

bd.load_model()
word = input("输入要搜索的关键词(个别词没有结果或不支持查询,输入BTC试试看): ")
start = input("输入开始日期(格式2018-09-09下同): ")
end = input("输入截至日期: ")
rst = bd.search(word, start, end)
print(rst)
