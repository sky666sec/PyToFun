# coding: utf-8
import re
import time
import asyncio
import aiohttp
import pyautogui

class DanmuServer():
	def __init__(self, roomid, csrf_token):
		self.url = "https://api.live.bilibili.com/ajax/msg"
		self.form = {"roomid":roomid, 
			"csrf_token":csrf_token}
		self.allow_keyboard_dicts = {'q':'q', 'w':'w', 'e':'e', 'r':'r',
									'w':'w', 'a':'a', 's':'s', 'd':'d', 'f':'f',
									"space":" "}
		self.allow_mouse_dicts = {"mlc":"left", "mrc":"right", "mmc":"middle"}

	def danmu_execution(self, dm):
		'''
		处理鼠标/键盘
		'''
		print(dm)
		dm_cmouse = re.findall(r".*?(mlc|mrc|mmc).*?", dm)
		dm_mmouse = re.findall(r".*?mmove\s*(\d+)\s+(\d+).*?", dm)
		dm_instructions = re.findall(r".*?(\w)(\d?).*?", dm)
		if dm_cmouse:
			pyautogui.click(button=self.allow_mouse_dicts[dm_cmouse[0]])
			time.sleep(0.3)
			return
		elif dm_mmouse:
			now_x, now_y = pyautogui.position()
			x = int(dm_mmouse[0][0]) if dm_mmouse[0][0] else now_x
			y = int(dm_mmouse[0][1]) if dm_mmouse[0][1] else now_y
			pyautogui.moveRel(x, y, duration=0.25)
			return
		if "space" in dm:
			dm_instructions = [("space", "")]
		if dm_instructions:
			cmd = dm_instructions[0]
			if cmd[0] in self.allow_keyboard_dicts.keys():
				if cmd[1]:
					time_wait = int(cmd[1])
				else:
					time_wait = int(1)
				pyautogui.keyDown(self.allow_keyboard_dicts[cmd[0]])
				time.sleep(time_wait)
				pyautogui.keyUp(self.allow_keyboard_dicts[cmd[0]])

	async def getDanmu(self):
		'''
		使用异步 请求api
		'''
		async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
			while True:
				print("连接弹幕网...(゜-゜)つロ 干杯~")
				async with session.post(self.url, data=self.form) as resp:
					print("获取弹幕数据...(゜-゜)つロ 干杯~")
					danmuData = await resp.json()
					# dm = [ (_tmp['nickname'], _tmp['text'], _tmp['timeline']) for _tmp in danmuData['data']['room'][-1:-6:-1] ]
					dm_text = danmuData['data']['room'][-1]['text']
					# self.push_danmu(data_list)
					print("获取弹幕数据成功...(゜-゜)つロ 干杯~")
					print("解析弹幕数据;并运行...(゜-゜)つロ 干杯~")
					self.danmu_execution(dm_text)
					# 太快了。我要减减速度
					time.sleep(0.3)


roomid = 3758547
csrf_token = "088056*********584eda17"

loop = asyncio.get_event_loop()
danmuserver = DanmuServer(roomid, csrf_token)
loop.run_until_complete(danmuserver.getDanmu())
loop.close()