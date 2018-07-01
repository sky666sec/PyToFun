#! /usr/bin/python3
# coding:utf-8
# auther:hyhmnn
'''
根据廖旭峰的图片验证码，
变成了一个算术验证码
'''
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

'''
#def range_zimu():
#	return chr(random.randint(65, 90))
'''
#返回一个验证图片的答案
def anser(a,b):
  return (a+b)
#生成一串验证的字符
def range_number():
	a = random.randint(0,9)
	b = random.randint(0,9)
	anser(a,b)
	numbers = str(a)+'+'+str(b)+'='
	return numbers

'''
#range_number()'s test
for a in range(5):
	print(range_number()[a])
'''
def rand_color():
	 return (random.randint(64, 255),\
	 		random.randint(64, 255), \
	 		random.randint(64, 255))
def rand_color2():
	 return (random.randint(32, 127),\
	 		random.randint(32, 127), \
	 		random.randint(32, 127))
#设置图片尺寸
width = 60 * 4
height = 60
#生成一个图片对象
image = Image.new('RGB',(width,height),(255,255,255))
#设置字体（使用的绝对路径）
font = ImageFont.truetype('C:\\Windows\\winsxs\\amd64_microsoft-windows-font-truetype-arial_31bf3856ad364e35_6.1.7601.17514_none_d0a9759ec3fa9e2d\\Arial.ttf',24)
#创建draw对象
draw = ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rand_color())
#把字符写入图中
range_number=range_number()
for t in range(4):
	draw.text((60*t + 10,10),range_number[t],font=font,fill=rand_color2())
#image = image.filter(ImageFilter.BLUR)
#保存图片abc.jpg 格式为jpeg  
image.save('abc.jpg', 'jpeg')
