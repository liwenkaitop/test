# 冒泡排序
def bubblesort(srcDatas):
	"""对一个列表中的数据进行从小到大的冒泡排序，返回排序成功"""
	if len(srcDatas)<=2:
		return True
	for i in range(0,len(srcDatas)-1):
		for j in range(0,len(srcDatas)-1-i):
			if srcDatas[j] > srcDatas[j+1]:
				data = srcDatas[j]
				srcDatas[j] = srcDatas[j+1]
				srcDatas[j+1] = data
	return True
