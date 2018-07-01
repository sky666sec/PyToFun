#! /usr/bin/python3
# coding:utf-8
# auther:hyhmnn

#test 1
'''
**数组祛除重复元素，
**一个盆友的练习。
O(n^n)
'''
a = ['a','b','c','b','a','d','c']
b = []
for i in a:
	if not i in b:
		b.append(i)
print(b)


b = list(set(a))

#test 2
'''
** 延时1s格式化打印系统当前时间
'''
import time
while True:
	print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
	time.sleep(1)
  


#test3
'''
**古典问题：
**有一对兔子，从出生后第3个月起每个月都生一对兔子，
**小兔子长到第三个月后每个月又生一对兔子，
**假如兔子都不死，问每个月的兔子总数为多少？
****我错误用题目的逻辑在逐步构建代码，（太蠢了以后要逻辑给理清楚）
'''
front = 1
behind= 1
for i in range(1,22):
	print('{} {}'.format(front,behind))
	front = front + behind
	behind = front + behind
#test4
'''
**判断101-200之间有多少个素数，并输出所有素数。
***做到烂的题目，今天发现else可以这样用，what？？？
O(nsqrt(n))这个怎么表示还不会？？？
'''
import math
number_list = []
for number in range(101,201):
	for i in range(2, int(math.sqrt(number)) +1 ): 
		if number %i == 0:
			break
	else:
		number_list.append(number)
print('{} {}'.format(len(number_list),number_list))

#test5
'''
题目：打印出所有的"水仙花数"，
所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
简单的就这样写主要是//符号（python相除都是浮点数）
O(n)
'''
import math
for number in range(100,1000):
	a = number // 100
	b = number // 10 % 10
	c = number % 10
	if number == a**3 + b**3 + c**3:
		print(number)

#test6
'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''
import string
strs = input('输入一行字符')
letters = 0
space = 0
digit = 0
others = 0
for a in strs:
	if a.isalpha():
		letters +=1
	elif a.isspace():
		space +=1
	elif a.isdigit():
		digit +=1
	else:
		others +=1

print('{} {} {} {}'.format(letters,space,digit,others))

#test7
'''
一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
好想官网答案有问题

'''
def ifyou(n,c):
	b=0
	for a in c:
		b+=a
	if b == n:
		return True
	else:
		return False
def reduceNum(n):
	c = []
	while n not in [1]:
		for a in range(2,n+1):
			if n%a ==0:
				n //= a
				if n ==1:
					c.append(n)
					c.append(a)
				else:
					c.append(a)
				break
	#print('{}={}'.format(n,c))
	return c
for number in range(2,1001):
	#print(reduceNum(number))
	if main(number,reduceNum(number)):
		print(number)
		print(reduceNum(number))
'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
程序源代码：
'''

#看到网上的冒泡算法，虽然输出结果没有什么变化， range居然可以把range（n+1,n）吞了，我要去好好的看看range的文档了。
a_s = input('three numbers')
a_lst = a_s.split(' ')

a_lst = [int(b) for b in a_lst]

#print (len(a_lst))
for c in range(len(a_lst)):
	for d in range(0,len(a_lst) -c -1):
		if a_lst[d] > a_lst[d+1]:
			a_lst[d] , a_lst[d+1] = a_lst[d+1] , a_lst[d]
print(a_lst)
#coding:utf-8
#根据要求打印
print('how len number?')
print ('1:平均数')
print('2:和')
print('3:exit')

while True:
	s = int(input('what you chiose number?'))
	if s == 3:
		break
	else:
		a = input('input you numbers(please use spcae ):')
		a_list = a.split(' ')
		#a_list[len(a_list)-1] !='' && a_list[len(a_list)-1] !=none
		#lst = [int(i) for i in a_list]
		#字符 转化 int
		if s==2:
			sum = 0
			for i in a_list:
				if i != None and i != '': 
					#简单的处理了，多打了空格，上面应该加检查字符是否是数字：
					xyf = int(i)
					sum = sum + xyf
			print (sum/len(a_list))	
		if s==1:
			sum = 0
			for i in a_list:
				if i != None and i != '':
					xyf = int(i)
					sum = sum + xyf
			print (sum)
#coding:utf-8

'''
Python 判读是不是等差数列，要求算法时间复杂度为O(NlogN)
不能用sort或sorted
我还是用了，而且时间复杂度我不知道怎么算。。。我太菜了，我要奋斗
问题： 判断等差数列
描述： 输入一个整数N，然后输入N个整数。判断这N个整数是否可以构建一个等差数列。（0<n<1000）
输入： 第一行为一个整数N，第二行为N个整数。
输出： 可以构成等差数列输出True，否则输出False。
示例：
(1)input： 10
5 3 2 1 7 6 4 8 10 9
output: True
(2)input： 5
4 6 3 2 7
output: False
'''
n = int(input('个数n：'))

number_s = input('numbers:')

number_slist =  number_s.split(' ')

number_list = [int(i) for i in number_slist]
'''
if len(number_slist) < n:
		print('缺失数字')
		while len(number_slist) >= n:
			number_s = input('numbers:')
			number_slist =  number_s.split('')
elif len(number_slist) > n:
	print('多了就取前n个')
	number_slist = number_slist[0:n]
	number_list = [int(i) for i in number_slist]
	take(number_list)
'''

def take(number_list):
#排序
	cont = 0
	number_list.sort()
	a = number_list[0] - number_list[1]

	for i in range(len(number_list)-1):
		b = number_list[i] - number_list[i+1]
		if a !=b and -a!=b:
			return ('output False')
		elif a==b or -a==b:
			cont += 1
	if cont == len(number_list) - 1:
		return ('output True')
print(take(number_list))
'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
程序源代码：
'''
#coding:utf-8
a = input('date:')
date = a.split('-')
day = [0,31,59,90,120,151,181,212,243,273,304,334,365]
if int(date[0]) % 4 :
	days = 0
else:
	days = 1
#print(days)
for b in range(int(date[1])):
	days += day[b]
days += int(date[2])
print (days)
'''
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
程序分析：
假设该数为 x。
1、则：x + 100 = n2, x + 100 + 168 = m2
2、计算等式：m2 - n2 = (m + n)(m - n) = 168
3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
7、接下来将 i 的所有数字循环计算即可。
程序源代码：
'''
x=[]
for a in range(1,85):
	if 168 % a == 0:
		b = 168/a
		if a > b and (a+b)%2==0 and (a-b)%2==0:
			m = (a + b) / 2
			n = (a - b) / 2
			x.append(n*n - 100)

print(x)
