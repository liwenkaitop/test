# -- coding: gbk --
import random
import unittest
# ����ķ�ʽ������ʱ����ֱ�ӵ��ú������ƣ�bubblesort
#from sort import bubblesort
# ����ķ�ʽ������ʱ��Ҫ��ģ������sort.bubblesort
import sort

class SortTestCase(unittest.TestCase):
	"""�����㷨�ĵ�Ԫ������"""
	
	def setUp(self):
		"""����һ����1000���������-1000��1000�����ɵ��б�����"""
		self.datas = []
		for i in range(0,1000):
			self.datas.append(random.randint(-1000,1000))
			
	def test_001_bubblesort(self):
		"""����ð������(����case)"""
		self.assertTrue(sort.bubblesort(self.datas))
		for i in range(0,999):
			self.assertTrue(self.datas[i]<=self.datas[i+1])
		
	def test_002_bubblesort(self):
		"""����ð������(�쳣case:�����ݻ�ֻ��1�����ݵ����)"""
		# �����ݲ���
		testdatas = []
		self.assertTrue(sort.bubblesort(self.datas))
		# һ�����ݲ���
		self.datas.append(random.randint(-1000,1000))
		self.assertTrue(sort.bubblesort(self.datas))
		
unittest.main()
