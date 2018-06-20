#! /usr/local/bin/python3
import uuid
import pyperclip
from pynput.keyboard import Key, Listener
from multiprocessing import Queue

q = Queue(2)

def on_press(key):
    # 监听按键
    if format(key) == 'Key.ctrl':
        # print('press{}'.format(key))
        q.put(1)
    if format(key) == 'Key.alt':
        # print('press{}'.format(key))
        q.put(2)
    if q.full():
        pyperclip.copy(str(uuid.uuid4()))

def on_release(keys):
    # 监听释放
    if format(keys) == 'Key.ctrl':
        q.get_nowait()
    if format(keys) == 'Key.alt':
        q.get_nowait()
    if keys == Key.esc:
        # Stop listener
        return False
if __name__ == '__main__':
    # 连接事件以及释放
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
