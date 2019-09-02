class Solution:
	def bubble_sort(self, data):
		for i in range(SIZE,-1,-1):
			for j in range(i):
				if data[j] > data[j+1]:
					data[j], data[j+1] = data[j+1], data[j]


class Solution1:
	# 两层遍历，每次找最小值
	def select_sort(self, data):
		for i in range(SIZE-1):
			min_dex = i
			for j in range(i+1, SIZE):
				if data[min_dex] > data[j]:
					min_dex = j
			data[i], data[min_dex] = data[min_dex], data[i]


class Solution2:
	# 两个指针，一个遍历未排序的数组，一个把数字放到排序好了的数组中
	def insert_sort(self, data):
		for i in range(1, size):
			tmp = data[i]
			no = i - 1
			while no >= 0 and tmp < data[no]:
				data[no+1] = data[no]
				no -= 1
			data[n+1] = tmp

	
class Solution3:
	# 中间逻辑和insert一样，只是用jmp去排序
	def shell_sort(self, data):
		jmp = SIZE//2
		while jmp != 0:
			for i in range(jmp, size):
				tmp = data[i]
				no = i - jmp
				while no >= 0 and tmp < data[no]:
					data[no+jmp] = data[no]
					no -= jmp
				data[no+jmp] = tmp
			jmp = jmp//2


class Solution4:
	def merge_sort():
		merge_select_sort(list1)
		merge_select_sort(list2)
		My_merge(SIZE1-1, SIZE2-1)

	def merge_select_sort(data):
		for i in range(SIZE-1):
			tmp = i
			for j in range(i+1, SIZE):
				if data[j] < data[tmp]:
					tmp = j
			data[j], data[tmp] = data[tmp], data[j]

	def My_merge(size1, size2):
		index1, index2 = 0, 0
		for index 3 in range(len(list1)+len(list2)-2):
			if list1[index1] < list2[index2]:
				list3.append(list1[index1])
				index1 += 1
			else:
				list3.append(list2[index2])
				index2 += 1
 

 class Solution5():
 	def quick_sort(data, lo, hi):
 		if lo >= hi:
 			return
 		
 		lf = lo
 		rg = hi
 		mid = data[lo]

 		while lf < rg:
 			while lf < rg and data[rg] >= mid:
 				rg -= 1
 			data[lf] = data[rg]
 			while lf < rg and data[lf] < mid:
 				lf += 1
 			data[rg] = data[lf]
 			
 		data[lf] = mid

 		quick_sort(data, lo, lf-1)
 		quick_sort(data, lf+1, hi)

class Solution5_1():
	def quick_so(data):
		if len(data) < 2:
			return data
		num = data[0]
		start = [x for x in data[1:] if x <= num]
		end = [x for x in data[1:] if x > num]
		return quick_so(start) + [num] + quick_so(end)


class Solution5():
	def radix(data):
		while n <= 100:
			tmp = [[0]*100 for row in range(10)]
			for i in range(size):
				m = (data[i]//n)%10
				tmp[m][i] = data[i]
			k = 0
			for i in range(10):
				for j in range(size):
					if tmp[i][j] != 0:
						data[k] = tmp[i][j]
						k += 1