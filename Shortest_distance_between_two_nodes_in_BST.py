'''
Given a Binary Search Tree and two keys in it. 
Find the distance between two nodes with given two keys. 
It may be assumed that both keys exist in BST.
'''

class newNode:
	'''
	def __init__(self, data):  
        self.val = data  
        self.left = None
        self.right = None
    '''

    def dis2(root, a, b):
    	if not root:
    		return 0
    	if root.val > max(a, b):
    		return dis(root.left, a, b)
    	if root.val < min(a, b):
    		return dis(root.right, a, b)
    	if a <= root.val <= b:
    		return disr(root, a) + disr(root, b)

    def disr(root, x):
    	if root.val = x:
    		return 0
    	elif root.val > x:
    		return 1 + disr(root.left, x)
    	else:
    		return 1 + disr(root.right, x)
    if a > b:
    	a, b = b, a
    return dis2(root, a, b)