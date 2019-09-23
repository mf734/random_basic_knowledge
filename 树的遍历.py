# 1. 中序遍历
# 1.1 递归实现中序遍历
def inorderT(self, root):
	if not root:
		return []
	return self.inorderT(root.left) + [root.val] + self.inorderT(root.right)



# 1.2 循环实现中序遍历，利用栈stack结构
# stack用来遍历，sol用来输出
# 用p去遍历，用stack记录回溯的位置
# 当p none了，说明刚刚遍历到左子结点
# 现在需要回溯到上一步，然后走上一步的右子树
def inorderT2(self, root):
	stack = []
	sol = []
	p = root
	while stack or p:
		if p:
			stack.append(p)
			p = p.left
		else:
			p = stack.pop()
			sol.append(p.val)
			p = p.right
	return sol



# 2. 前序遍历和后序遍历
# 2.1.1 递归实现前序遍历
def preorderT(self, root):
	if not root:
		return []
	return [root.val] + self.preorderT(root.left) + self.preorderT(root.right)

# 2.1.2 递归实现后序遍历
def posorderT(self, root):
	if not root:
		return []
	return self.posorderT(root.left) + self.posorderT(root.right) + [root.val]

# 2.2.1 循环实现前序遍历
# 立即打印当前结点，并push右子结点入栈
# 遍历到其左子结点
# 当前结点非none，每一次循环将当前结点入栈
# 当前结点为none，则出栈一个结点
def preorderT2(self, root):
	stack = []
	sol = []
	p = root
	while stack or p:
		if p:
			sol.append(p.val)
			stack.append(p.right)
			p = p.left
		else:
			p = stack.pop()

# 2.2.2 循环实现后序遍历
# 原理和前序很近
def posOrderT2(self, root):
	stack = []
	sol = []
	p = root
	while stack or p:
		if p:
			sol.append(p.val)
			stack.append(p.left)
			p = p.right
		else:
			p = stack.pop()
	return sol[::-1]



# 3.层次遍历（宽度优先）
# 3.1 递归实现 (从左到右）
# 递归函数有一个level，表示结点当前的层数
def levelOrder(self, root):
	def helper(node, level):
		if not node:
			return
		else:
			sol[level-1].append(node.val)
			# 遍历到新层时，只有最左边的结点使得等式成立
			# 也就是新一层的第一个结点
			# 建立空的，为下一层做准备
			if len(sol) == level:
				sol.append([])
			helper(node.left, level+1)
			helper(node.right, level+1)
	sol = [[]]
	helper(root, 1)
	return sol[::-1]

# 如果是从右到左，只需要互换left和right就行
# 这样就会以right的第一个为以上if的判断点
# 拓展：还可以zigzag遍历：层数为奇偶时，用append和insert(0)


# 3.2 循环实现，使用队列
# 每一层都需要打印
# 每打印结点都会在队列中依次添加两个子结点
# 每一层的顺序一样
# 所以FIFO
def levelOrder2(self, root):
	if not root:
		return []
	sol = []
	p = root
	queue = [p]
	while queue:
		p = queue.pop(0)
		sol.append(p.val)
		if p.left:
			queue.append(p.left)
		if p.right:
			queue.append(p.right)
	return sol



# 4.二叉树结点个数
def treeNode(self, root):
	if not root:
		return 0
	nums = treeNode(root.left)
	nums += treeNode(root.right)
	return nums + 1



# 5.二叉树的最大深度
def TreeDepth(self, root):
	if not root:
		return 0
	ld = TreeDepth(root.left)
	rd = TreeDepth(root.right)
	return (max(ld, rd) + 1)