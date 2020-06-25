# -- coding: gbk --
import random
import unittest
# 下面的方式，调用时可以直接调用函数名称：bubblesort
#from sort import bubblesort
# 下面的方式，调用时需要用模块名：sort.bubblesort
import sort

class SortTestCase(unittest.TestCase):
	"""排序算法的单元测试类"""
	
	def setUp(self):
		"""生成一个由1000个随机数（-1000，1000）构成的列表数据"""
		self.datas = []
		for i in range(0,1000):
			self.datas.append(random.randint(-1000,1000))
			
	def test_001_bubblesort(self):
		"""测试冒泡排序(正常case)"""
		self.assertTrue(sort.bubblesort(self.datas))
		for i in range(0,999):
			self.assertTrue(self.datas[i]<=self.datas[i+1])
		
	def test_002_bubblesort(self):
		"""测试冒泡排序(异常case:空数据或只有1个数据的情况)"""
		# 空数据测试
		testdatas = []
		self.assertTrue(sort.bubblesort(self.datas))
		# 一个数据测试
		self.datas.append(random.randint(-1000,1000))
		self.assertTrue(sort.bubblesort(self.datas))
		
unittest.main()
