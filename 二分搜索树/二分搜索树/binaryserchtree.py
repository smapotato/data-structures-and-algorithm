from multiprocessing import Queue


class TreeNode():
    def __init__(self, key, val, left=None, right=None,
                 parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def insert(self, key, value):  # 插入节点
        if self.root:
            self._insert(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size = self.size + 1

    def _insert(self, key, value, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._insert(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, value, parent=currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._insert(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value, parent=currentNode)
        else:
            currentNode.key = key

    def __setitem__(self, key, value):  # 重载赋值的[]运算符
        self.insert(key, value)

    def get(self, key):  # 查找节点
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, item):  # 重载in运算符
        if self._get(item, self.root):
            return True
        else:
            return False

    def preOrder(self,node):  # 前序遍历
        print(node.key)
        if node.leftChild:
            self.preOrder(node.leftChild)
        if node.rightChild:
            self.preOrder(node.rightChild)

    def inOrder(self,node):  # 中序遍历,从小到大
        if node.leftChild:
            self.inOrder(node.leftChild)
        print(node.key)
        if node.rightChild:
            self.inOrder(node.rightChild)

    def postOrder(self,node):  # 后序遍历,释放节点
        if node.leftChild:
            self.leftChild.post0rder()
        if node.rightChild:
            self.rightChild.preOrder()
        print(node.key)

    def levelOrder(self):  # 层序遍历，有队列实现，节点的先后顺序
        q = Queue()
        q.put(self.root)
        while not q.empty():
            node = q.get()
            print(node.key)
            if node.hasLeftChild():
                q.put(node.leftChild)
            if node.hasRightChild():
                q.put(node.rightChild)

    def findMin(self):  # 找到最小节点
        current = self.root
        while current.hasLeftChild():
            current = current.leftChild
        return current.key

    def findMax(self):  # 找到最大节点
        current = self.root
        while current.hasRightChild():
            current = current.rightChild
        return current.key

    def delete(self, key):  # 删除键
        if self.size > 1:
            nodeTORrmove = self._get(key, self.root)
            if nodeTORrmove:
                self.remove(nodeTORrmove)
                self.size -= 1
            else:
                return "Error,key not in tree"
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            return "Error,key not in tree"

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():  # 没有子节点
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # 有两个子节点
            succ = currentNode.findSuccessor()
            succ.spliceout()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:  # 只有一个子节点
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

    def findSuccessor(self):
        succ = self.rightChild.findMin()  # 找到右子树的最小节点
        return succ

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        else:
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"
mytree[9]="zed"
mytree[10]="ashe"
del mytree[10]
print(mytree.levelOrder())
