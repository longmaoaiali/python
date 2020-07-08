from random import randint
from threading import Thread
from time import time, sleep

class DownloadTask(Thread):
	def __init__(self, filename):
		super().__init__()
		self._filename = filename
		
	def run(self)
		print('start download ' % self._filename)
		time_to_download = randint(5,10)
		sleep(time_to_download)
		print('download %s complete, spend %d seconds' % (self._filename, time_to_download))

def main():
	start = time()
	t1 = DownloadTask('Python从入门到住院.pdf')
	t1.start()
	t2 = DownloadTask('Peking Hot.avi')
	t2.start()
	
	t1.join()
	t2.join()
	
	end = time()
	print('totally spend %d seconds' % (end - start))

if __name__ == '__main__'
	main()