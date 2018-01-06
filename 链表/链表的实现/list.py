class Node:  # 节点
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnoederedList():
    # 链表类本身不包含任何节点对象，它只包含对链接结构中一个节点的单个引用
    # 链表的头指代列表的第一项的第一个节点，该节点保存对下个节点的引用
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None  # 链表中没有节点时才为真，新链表为空

    def add(self, item):
        temp = Node(item)  # 创建新节点
        # 将新节点链接到现有结构中
        temp.setNext(self.head)  # 更改节点的下一个引用以引用旧链表的第一个节点
        self.head = temp  # 修改链表的头以引用新节点

    def size(self):
        current = self.head
        count = 0
        while current:  # 当引用没到链表的结束位置(None)
            count += 1
            current = count.getNext()
        return count

    def search(self, item):  # 查看item是否在链表中
        current = self.head
        while current:
            if current.getData() == item:
                return True
            else:
                current = current.getNext()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext
        if previous == None:  # 删除的项是链表中的第一个项
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
