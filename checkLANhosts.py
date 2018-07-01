#! /usr/bin/python3
# coding:utf-8
# auther:hyhmnn
# date:2017-12-30
'''
can run in win/linux

	Find the host that can be Ping through in the LAN
--------------------------------
直接运行
输入局域网网关
使用的多进程，进程池为30
'''
import os
import platform
from multiprocessing import Pool


def ping_hostname(hostnumber, gateway):
	hostname=gateway+str(hostnumber)
	comm, hint_info = winORlinux(hostname)
	
	fd = os.popen(comm)
	fdread=fd.read()
	result = '{hostname} is {state}'
	
	if not hint_info in fdread:
		print(result.format(hostname=hostname,state='up'))

def winORlinux(hostname):
	sysstr = platform.system()
	
	if sysstr == "Windows":
		comm = 'ping -n 1 {hostn}'.format(hostn=hostname)
		hint_info = '无法访问目标主机'
	elif sysstr == "Linux":
		comm = 'ping -c 1 {hostn}'.format(hostn=hostname)
		hint_info = 'Unreachable'
	
	return comm,hint_info

def main():
	gateways = ('input gateway.\nlike this (192.168.1.1):')
	gateway =''
	for a in  gateways.split('.')[:-1]:
		gateway += a+'.'

	p = Pool(30)
		#30
	for hostnumber in range(1,256):
		p.apply_async(ping_hostname,args=(hostnumber,gateway,))
	print('wait ...')
	p.close()
	p.join()
	print('done.')

if __name__ == '__main__':
	main()
