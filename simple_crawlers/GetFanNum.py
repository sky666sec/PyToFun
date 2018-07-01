'''
闲着无聊爬了一个“宅男福利社”网站一个番号网页
过有缺陷，会出现514错误，无法通过服务器验证,需要导入cookies
相信我会继续完善~
'''
from bs4 import BeautifulSoup
import re
import requests

def getHtmlText(url,code = 'utf-8'):
	try:
		tk = {'user-agent':'Mazilla/5.0'}
		r = requests.get(url,timeout = 60,headers = tk)
		r.raise_for_status()
		r.encoding = code
		return r.text
	except:
		return ''
def get_fanurls(fanurls,html):
#所有的url，
	try:
		soup = BeautifulSoup(html,'html.parser')
		article = soup.find_all('a',attrs = {'class':'fancyimg home-blog-entry-thumb'})
		for i in article:
			href = i.attrs['href']
			fanurls.append(re.findall(r'[a-z]+://[^\s]*\.html',href))
	except:
		print('error 2')

def get_fan_numbers(fanurls,fan_numbers):
	for url in fanurls:
		try:
			print(url[0])
			html = getHtmlText(url[0])
			#print(html)
			soup = BeautifulSoup(html,'html.parser')
			div = soup.find('div',attrs = {'class':'single-text'})
			print(type(div))
			ppp = div.find_all('p')
			for i in range(len(ppp)):
				fans = re.findall(r'番号：[A-Z]{2,4}-\d{2,4}',ppp[i].text)
				if fans != []:
					fan_numbers.append(fans[0])
		except:
			continue
		#continue
		#if div[0] is not None and str(div) is not '':
		#	print(len(str(div[0])))
		#print(len(div))
		#fan_numbers.append(re.findall(r'番号：[A-Z]{2,4}-\d{2,4}',html))

def main():
	url = 'http://www.zhainanfulishe.net/tag/%E7%95%AA%E5%8F%B7/'
	fanurls = []
	fan_numbers = []
	for a in range(1,6):
		true_url = url + "page/" + str(a)
		html = getHtmlText(true_url)
		#print(true_url,fanurls)

		get_fanurls(fanurls,html)
	get_fan_numbers(fanurls,fan_numbers)
	print(fan_numbers,len(fan_numbers),len(fanurls))
main()
