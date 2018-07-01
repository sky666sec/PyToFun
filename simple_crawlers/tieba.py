#! /usr/bin/python3
'''
简答的爬了'http://tieba.baidu.com/p/5225596016'上的图片
不过现在这个贴子被删了
'''
import requests
import re
from bs4 import BeautifulSoup


def get_html(url,code='utf-8'):
	try:
		r = requests.get(url,timeout = 60)
		r.raise_for_status()
		r.encoding = code
		return r.text
	except:
		return 'none'

def make_soup(html):
	soup = BeautifulSoup(html,'html.parser')
	image_soup = soup.find_all('img',attrs={'class' : 'BDE_Image'})
	#print(image_soup)
	image_urls=[]
	for image_ini in image_soup:
		image_url = re.findall(r'http://.*.jpg',str(image_ini))[0]
		image_urls.append(image_url)
	return image_urls


def download_image(image_urls):
	cont = 0
	for image_url in image_urls:
		imageR = requests.get(image_url)

		with open('GirlsAvatarLibrary/%s.jpg'%cont,'wb') as file:
			file.write(imageR.content)
			#(imageR.content	写入二进制数据)
			file.close()
		cont += 1

def main(url):
	image_urls = []
	html = r=get_html(url)
	image_urls = make_soup(html)
	download_image(image_urls)

if __name__ == '__main__':
	url = 'http://tieba.baidu.com/p/5225596016'
	main(url)
