#! /usr/bin/python
# coding:utf-8

import masscan
import json

def main(hosts, ports, arguments=''):
	'''
	1-install masscan
		$ sudo apt-get install git gcc make libpcap-dev
		$ git clone https://github.com/robertdavidgraham/masscan
		$ cd masscan
		$ make

	2-$ pip install python-masscan
	
	3-Close BUG
		in /usr/local/lib/python2.7/dist-packages/masscan/masscan.py
		change to:
			logger.setLevel(logging.NOTSET)

	3-add PATH
		echo "export PATH=$PATH:/[Your installation directory]/masscan/bin" >> /etc/profile
		source /etc/profile

	4-use root run
	'''
	mas = masscan.PortScanner()
	result = mas.scan(hosts, ports=ports, arguments=arguments)
	return json.dumps({'result':result['scan']}, separators=(',', ':'))

if __name__ == '__main__':
	# arguments='--max-rate 1000'
	result = main("192.168.1.0/24", ports="80,8080,21,21")
	print result
