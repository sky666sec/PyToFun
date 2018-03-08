`无聊就写写小脚本提高兴趣，继续学习python`

`^-^`

* [MysqlSqlServeHelper.py](https://github.com/hyhmnn/InterestingScript/blob/master/MysqlSqlServeHelper.py)
```python3
#0x01:MysqlHelper.py
#用法:

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
  SqlSerHelper 注意的是:
  params = (strings,)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```
* [option_parser_test.py](https://github.com/hyhmnn/InterestingScript/blob/master/option_parser_test.py) 
```python3
# 0x02:option_parser_test.py
# 简单使用optparse模块
# +++++++++++++++++++++++++++++++++++====================+++++++++++++++++++++=================
```
* [OpenXlsx.py](https://github.com/hyhmnn/InterestingScript/blob/master/OpenXlsx.py)
```python3
# 0x03:OpenXlsx.py
# 用法：
  member_infos = OpenXlsx("test.xlsx", "Sheet1")
  num = member_infos.lines()
  for n in range(num):
    context_list = member_infos.Acolumn(n)
    print(context_list)
```
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
[生成验证码](https://github.com/hyhmnn/PythonScripts/blob/master/VerCode.py)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
[监控linux本地磁盘，通过邮箱告知](https://github.com/hyhmnn/PythonScripts/blob/master/DiskAlarm.py)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```
定时用微信发送天气的信息（因为我没有两个微信，我就发送到公众号了）
爬虫:用的requests+bs4+re基础方法
爬取的天气网站是http://www.weather.com.cn/weather/101190201.shtml
wechat:使用的wxpy库
定时就自己简单的搞了一下
```
[GETWeaInfo.py](https://github.com/hyhmnn/PythonScripts/blob/master/GETWeaInfo.py)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
