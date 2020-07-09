from time import time
from threading import Thread

import requests

class DownloadHandler(Thread):
	def __init__(self, url):
		super().__init__()
		self.url = url
		
	def run(self):
		filename = self.url[self.url.rfind('/') + 1:]
		resp = requests.get(self.url)
		with open('/Users/demo/'+filename, 'wb') as f:
			f.write(resp.content)

def main():
	resp = requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')
	data_model = resp.json()#JSON数据格式转化为字典
	for mm_dict in data_model['newslist']:
		url = mm_dict['picUrl']
		#mutliThread to download picture
		DownloadHandler(url).start()

if __name__ == '__main__'
	main()