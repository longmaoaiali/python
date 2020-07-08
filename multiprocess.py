from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
	print('start download , pid = %d.' % getpid())
	time_to_download = randint(5,10) #随机生成整数：[a-b]区间的整数（包含两端）
	sleep(time_to_download)
	print('download file spend %d' % time_to_download)
	

def main():
	start = time()
	p1 = Process(target=download_task, args=('Python 从入门到精通', ))
	p1.start()
	p2 = Process(target=download_task, args=('1.avi', ))
	p2.start()
	
	p1.join() #等待子进程结束再继续向下执行
	p2.join()
	
	end = time()
	print('totally spend %.2f seconds' % (end-start))
	

if __name__ == '__main__':
	main()