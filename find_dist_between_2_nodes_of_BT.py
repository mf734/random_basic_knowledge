class Node: 
	'''def __init__(self, val): 
		self.val = val 
		self.right = None
		self.left = None'''
	def pathN(root, path, k):
		if not root:
			return False
		path.append(root.val)
		if root.val == k:
			return True
		if (root.left and pathN(root.left, path, k)) or (root.right and pathN(root.right, path, k)):
			return True
		else:
			path.pop()
			return False

	def dis(root, d1, d2):
		if root:
			path1 = []
			pathN(root, path1, d1)
			path2 = []
			pathN(root, path2, d2)
			i = 0
			while i < len(path1) and i < len(path2):
				if path1[i] != path2[i]:
					break
				i += 1
			return (len(path1)+len(path2)-2*i)
		else:
			return 0

