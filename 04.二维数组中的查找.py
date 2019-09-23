# 方法一：循环迭代查找
class Solution:
	def Find(self, target, array):
		if not array:
			return
		row = len(array)
		col = len(array[0])
		for i in range(row):
			for j in range(col):
				if target == array[i][j]:
					return True
		return False
# 暴力法简单版：
	def Find1(self, array, target):
		for row in array:
			if target in row:
				return True
		return False


# 二层遍历，从右上角
class Solution:
	def Find(self, target, array):
		if len(array) == 0 or len(array[0]) == 0:
			return False
		i, j = 0, len(array[0])-1

		while i < len(array[0]) and j >= 0:
			if array[j][i] < target:
				i += 1
			elif array[j][i] > target:
				j -= 1
			else:
				return True
		return False