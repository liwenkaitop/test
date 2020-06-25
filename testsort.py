# -- coding: gbk --
import random
import unittest
import allure
import sort

class SortTestCase(unittest.TestCase):
	"""sort algorithms unittest"""
	
	def setUp(self):
		"""generate 1K random number list range (-1000，1000）"""
		self.datas = []
		for i in range(0,1000):
			self.datas.append(random.randint(-1000,1000))

	@allure.description("test bubble sort(normal case:1000 numbers)")
	def test_001_bubblesort(self):
		self.assertTrue(sort.bubblesort(self.datas))
		for i in range(0,999):
			self.assertTrue(self.datas[i]<=self.datas[i+1])

	@allure.description("test bubble sort(abnormal case: null)")
	def test_002_bubblesort(self):
		# 空数据测试
		testdatas = []
		self.assertTrue(sort.bubblesort(self.datas))

	@allure.description("test bubble sort(abnormal case: one number)")
	def test_003_bubblesort(self):
		# 一个数据测试
		self.datas.append(random.randint(-1000,1000))
		self.assertTrue(sort.bubblesort(self.datas))
		
unittest.main()
