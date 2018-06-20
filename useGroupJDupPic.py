#! /usr/local/bin/python3
import os
import requests
import pyperclip
from subprocess import call
from multiprocessing import Queue
from pynput.keyboard import Key, Listener

q = Queue(2)

def upfiel2JD(filename):
    try:
        with open(filename, 'rb') as file:
            url = 'https://group.jd.com/ueditor/jsp/imageUp.jsp?action=uploadimage&encode=utf-8'
            headers = {
                'Host': 'group.jd.com',
                'Origin': 'https://group.jd.com',
                'Referer': 'https://group.jd.com/ueditor/dialogs/imag',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',   
            }
            response = requests.post(url, headers=headers,files={'upfile':file})
            return '![](%s)'%('http://img30.360buyimg.com/club_community/'+response.json()['url'])
    except:
        return "获取图片失败"

def getCopyFile():
    try:
        call(['/usr/local/bin/pngpaste', '-v'], stderr=open('/dev/null', 'w'))
    except OSError:
        print('使用命令安装`brew install pngpaste`.')
        sys.exit()
    filename = "test.png"
    file_path = os.path.join('/tmp', filename)
    save = call(['/usr/local/bin/pngpaste', file_path])
    if save:
        return '' 
    return file_path

def on_press(key):
    # 监听按键
    if format(key) == 'Key.ctrl':
        # print('press{}'.format(key))
        q.put(1)
    if format(key) == 'Key.shift':
        # print('press{}'.format(key))
        q.put(2)
    if q.full():
        pyperclip.copy(upfiel2JD(getCopyFile()))

def on_release(keys):
    # 监听释放
    if format(keys) == 'Key.ctrl':
        q.get_nowait()
    if format(keys) == 'Key.shift':
        q.get_nowait()
    if keys == Key.esc:
        # Stop listener
        return False


if __name__ == '__main__':
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()useGroupJDupPic.py
