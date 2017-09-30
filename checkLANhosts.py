'''
win下
直接运行
输入局域网网关
使用的多进程，进程池为30
'''
import os
from multiprocessing import Pool

def ping_hostname(hostnumber,gateway):
		hostname=gateway+str(hostnumber)
		fd = os.popen('ping -n 1 {hostname}'.format(hostname=hostname))
		fdread=fd.read()
		result = '{hostname} is {state}'
		if '无法访问目标主机'not in fdread:
			print(result.format(hostname=hostname,state='up'))


if __name__ == '__main__':
	gateways = input('input gateway.\nlike this (192.168.1.1):')
	gateway =''
	for a in  gateways.split('.')[:-1]:
		gateway += a+'.'

	p = Pool(30)
#30
	for hostnumber in range(1,255):
		p.apply_async(ping_hostname,args=(hostnumber,gateway,))
	print('wait ...')
	p.close()
	p.join()
	print('done.')	
