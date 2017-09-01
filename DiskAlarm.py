# -*- coding:utf-8 -*- 
'''
监控linux本地磁盘，通过邮箱告知
运行环境 centos 6 	python3.6.0 && python 2.7
@hyhmnnn
2017-5-24
QQ邮箱发送是看到知乎上的小哥===知乎： 邓旭东HIT

'''
import os
import datetime
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

def check_disc():
#获取linux系统的磁盘内容
	str_data = os.popen('df -h |grep /|awk \'{print $6,$5}\'').read()
	str_data = str_data.split('\n')

	str_abc = []
	str_def = []
#对获取的列表进行简单处理
	for a in str_data:
		if a !=None and a != '':
			a = a.split(' ')
			str_abc.append(a)
#判断磁盘的使用率
	for b in range(len(str_abc)):
		d = str_abc[b][1].split('%')
		c = int(d[0])
		if c >= 60:
			str_def.append(str_abc[b][0])
			str_def.append(str_abc[b][1])
		else:
			str_def.append(str_abc[b][0])
			str_def.append('ok')
	return str_def
def clear_xuanwo(rmdir_path):
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	#在得知使用率超过了阀值时
	#删除指定磁盘挂载下的目录中大于30天的文及目录
	path_dir = 'find '+rmdir_path+'/* -mtime +30 -exec rm -rf {} \;'
	os.popen(path_dir)

	write_log(now +': %s was Deleted\n'%rmdir_path)

def write_log(log_text):
		path_s = os.getcwd()
		path_s = path_s+'/mail-alarm.log'
		# windows 下的路径名斜杠“\”需要用这个注释\
		#C:\\
		if os.path.exists(path_s):
			log_file = open(path_s,'a')
			log_file.write(log_text)
			log_file.close()
		else:
			log_file1 = open(path_s,'w')
			log_file1.write(log_text)
			log_file1.close()

def send_mail(receiver_mail,title_txt,content_txt):	
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	#定义一些变量
	host_server = 'stmp.qq.com'
	
	sender_qq = '*1212312**'
	
	pwd = ''
	
	sender_qq_mail = '2***3123**@qq.com'
	
	receiver = receiver_mail
	
	mail_content = content_txt
	
	mail_title = title_txt
	'''
	发送邮件
	网络连接有风险
	异常处理很重要
	'''
	try:
		smtp = SMTP_SSL(host_server)
		
		smtp.set_debuglevel(1)
		smtp.ehlo(host_server)
		smtp.login(sender_qq, pwd)

		msg = MIMEText(mail_content, "plain", 'utf-8')
		msg["Subject"] = Header(mail_title, 'utf-8')
		msg["From"] = sender_qq_mail
		msg["To"] = receiver
		smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
		smtp.quit()

		write_log(now +': mail send ok\n')
		#加个回车好看些
	except:
		write_log(now +': Mailbox connection error\n')
def main():
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	str_cip = []
	str_cip = check_disc()
	for a in range(len(str_cip)-1):
		if str_cip[a+1] != 'ok':
			text1 = '快来人啊，有个东西爆啦BOOM'
			text = '我已经自动删除了30天前的文件及文件夹。'
			clear_xuanwo(str_cip(a))
			send_mail(receiver@qq.com,text1,'%s 磁盘使用率达到了%s'%str_cip[a],%str_cip[a+1]+text)
		elif:
			write_log(now +': disc is ok\n')

if __name__ == '__main__':
	mian()
