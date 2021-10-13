#使用@property包装器来包装getter和setter方法
#@property装饰器就是负责把一个方法变成属性调用的
#参考 https://www.liaoxuefeng.com/wiki/1016959663602400/1017502538658208
class Person(object):
	
	def __init__(self, name, age):
		self._name = name
		self._age = age
		
	# 访问器 - getter方法
	@property #负责将一个方法变成属性调用
	def name(self):
		return self._name
	
	# 访问器 - getter方法
	@property #负责将一个方法变成属性调用
	def age(self):
		return self._age
	
	# 修改器 - setter方法
	@age.setter #将一个setter方法变成属性赋值
	def age(self, age):
		self._age = age
		
	def play(self):
		if self._age <= 16:
			print('%s正在玩飞机' % self._name)
		else:
			print('%s正在斗地主' % self._name)
			
def main():
	person = Person('王大锤', 12)
	person.play()
	person.age = 25
	person.play()
	
	
if __name__ == '__main__':
	main()