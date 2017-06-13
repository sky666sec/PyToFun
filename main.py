import requests
import re
from bs4 import BeautifulSoup
import time
from wxpy import *
import sched

def wxBotlogin():
	bot = Bot(console_qr = 2)
	return bot
	
def wxBotSendTxt(bot,send_txt):
	best_love = bot.mps().search('***我写的是公众号的名字***')[0]
	best_love.send(send_txt)
	
def getHtmlText(url,code = 'utf-8'):
	try:
		r = requests.get(url,timeout = 60)
		r.raise_for_status()
		r.encoding = code
		#print(len(r.text))
		return r.text
	except:
		return ''
def getWeatherInfo(html):
	try:
		wstr = ''
		soup = BeautifulSoup(html,'html.parser')
		soupl = soup.find_all('li',attrs = {'class':'on'})[1]
		str1 = re.findall(r'>(.*)</',str(soupl))
		b = ''
		try:
			slist = re.findall(r'^(.*)</span>(.*)<i>(.*)$',str1[4])
			for x in range(len(slist[0])):
				b += slist[0][x]
		except:
			b = str1[4]
		str1[4] = b

		for i in str1:
			if i != '':
				wstr = wstr +i + '\n'
		if '雨' in wstr:
			wstr += '今天别忘记带雨伞 ^.^\n'
		
		return wstr
	except:
		return 'sorry hanpped error\n'
'''
def main():
	url = 'http://www.weather.com.cn/weather/101190201.shtml'
	html = getHtmlText(url)
	wstr = getWeatherInfo(html)
	wstr += time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	bot = wxBotlogin()
	wxBotSendTxt(bot,wstr)
'''
	
xyf = wxBotlogin()
weather_url = 'http://www.weather.com.cn/weather/101190201.shtml'

def main(bot,url):
	html = getHtmlText(url)
	wstr = getWeatherInfo(html)
	wstr += time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	wxBotSendTxt(bot,wstr)
#####################################
b = ['22:29','22:28','22:27','8.18','8:19','8:20','8:21','8:22']#你的时间表
while True:
	a = time.strftime('%H:%M',time.localtime(time.time()))
	if a in b:
		main(xyf,weather_url)
		time.sleep(60)
	


	#timming_exe(xyf,weather_url,inccc)
