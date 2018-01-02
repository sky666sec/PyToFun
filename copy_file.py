import os
from multiprocessing import Pool,Manager
import time

class CopyFile(object):
	def __init__(self, folderename):
		self.old_folderename = folderename
		self.new_folderename = self.old_folderename + "_back"
		self.queue = Manager().Queue()
		self.files = []

	def mkdir_new_folder(self):
		os.mkdir(self.new_folderename)

	def obtain_files(self):
		self.files = os.listdir(self.old_folderename)

	def copy_content(self, filename):
		fr = open(self.old_folderename+"/"+filename)
		fw = open(self.new_folderename+"/"+filename,"w")

		content = fr.read()
		fw.write(content)
		fr.close()
		fw.close()
		# print(filename)
		self.queue.put(filename)
		time.sleep(1)
		# 文件太少
	
	def task(self):
		pool = Pool(5)

		for file in self.files:
			pool.apply_async(self.copy_content,(file,))
		
		# pool.close()
		# pool.join()
   # 显示进度-------------------------------
		allNum = len(self.files)
		num = 0
		while num < allNum:
			time.sleep(0.5)
			# 文件太少
			self.queue.get()
			num += 1
			copyRate = (num/allNum)*100
			print("\rcopy[%.2f%%]"%copyRate,end="")
      
			print("copy complete..")
   # 显示进度-------------------------------
def main():
	fname = input("folder name:")
	copy_test = CopyFile(fname)
	
	copy_test.mkdir_new_folder()
	copy_test.obtain_files()
	copy_test.task()

if __name__ == '__main__':
	main()
