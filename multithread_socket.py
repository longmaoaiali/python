from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread

def main():
	class FileTransferHandler(Thread):
		def __init__(self, client):
			super().__init__()
			self.client = client
			
		def run(self):
			my_dict = {}
			my_dict['filename'] = 'guido.jpg'
			my_dict['filedata'] = data
			json_str = dumps(my_dict) # change dict to json data
			self.client.send(json_str.encode('utf-8'))
			self.client.close()
			

	server = socket()
	server.bind(("192.168.1.100", 5566))
	server.listen(512)
	with open('guido.jpg', 'rb') as f:
		data = b64encode(f.read()).decode('utf-8') ## 将二进制数据处理成base64再解码成字符串
		
	while True:
		client, addr = server.accept()
		FileTransferHandler(client).start()

if __name__ == '__main__'
	main()
	
"""
from socket import socket
from json import loads
from base64 import b64decode

def main():
	client = socket()
    client.connect(('192.168.1.100', 5566))

	in_data = bytes()
	data = client.recv(1024)
    while data:
        # 将收到的数据拼接起来
        in_data += data
        data = client.recv(1024)
	
    # 将收到的二进制数据解码成JSON字符串并转换成字典
    # loads函数的作用就是将JSON字符串转成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('/Users/Hao/' + filename, 'wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))
    print('图片已保存.')
if __name__ == '__main__':
    main()
"""