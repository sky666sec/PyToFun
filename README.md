`无聊就写写小脚本提高兴趣，继续学习python`

`^-^`

- [MysqlSqlServeHelper.py](./MysqlSqlServeHelper.py)
```python
from MysqlSqlServeHelper import MysqlHelper, SqlSerHelper
helper=MysqlHelper('localhost',3306, 'students', 'root','123456')
  # 多查询
sql='select name,gender from students order by id desc'
result=helper.get_all(sql, [])
print(result)
  # 操作数据
sql2 = "update students set name=%s where id=%s"
params = ["yes",1]
conn = helper.update(sql2,params)
print(conn)
  #-------------------------------
# SqlSerHelper 注意的是:
# params = (strings,)
```
- [openXlsx.py](./openXlsx.py)
```python
import openXlsx
member_infos = OpenXlsx("test.xlsx", "Sheet1")
num = member_infos.lines()
for n in range(num):
  context_list = member_infos.Acolumn(n)
  print(context_list)
```
- [生成验证码](./VerCode.py)
```
根据廖旭峰的图片验证码，
变成了一个算术验证码
```
- [监控linux本地磁盘，通过邮箱告知](./DiskAlarm.py)
- [简单爬虫集合](./simple_crawlers)
- [checkLANhosts.py](./checkLANhosts.py)
```
can run in win/linux

	Find the host that can be Ping through in the LAN
--------------------------------
直接运行
输入局域网网关
使用的多进程，进程池为30
```
- [copy_file](./copy_file.py)
> 多进程拷贝文件

- [GETWeaInfo.py](./GETWeaInfo.py)
```
定时用微信发送天气的信息（因为我没有两个微信，我就发送到公众号了）
爬虫:用的requests+bs4+re基础方法
爬取的天气网站是http://www.weather.com.cn/weather/101190201.shtml
wechat:使用的wxpy库
定时就自己简单的搞了一下
```
---
emmmm...2018-07-02整理了一下，发现以前写的太水了...现在我要努力提高代码水平了...
