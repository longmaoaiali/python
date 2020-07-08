from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
	print('start download %d' % filename)
	time_to_download  = randint(5,10)
	sleep(time_to_download)
	print('download complete %d' % time_to_download)

def main():
	start = time()
	t1 = Thread(target=download, args=('python从入门到精通', ))
	t1.start()
	t2 = Thread(target=download, args=('1.mp4', ))
	t2.start()
	
	t1.join()
	t2.join()
	
	end = time()
	print('totally spend %d seconds' % (end-start))

if __name__ == '__main__'
	main()