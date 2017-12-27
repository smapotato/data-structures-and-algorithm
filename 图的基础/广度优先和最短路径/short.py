class ShoretestPath():  # 广度优先遍历和最短路径
    def __init__(self, graph, s):
        self.G = graph  # 图
        self.s = s  # 从s节点开始寻找其它节点的路径
        self.visited = [False for _ in range(self.G.V())]  # 记录每个节点是否被插入队列
        self.fromed = [-1 for _ in range(self.G.V())]  # 记录此节点来自哪个节点的连接
        self.ord = [-1 for _ in range(self.G.V())]  # 记录s节点到每一个节点的距离
        q = Queue()
        q.put(s)
        self.visited[s] = True
        self.ord[s] = 0
        while not q.empty():
            v = q.get()
            adj = self.G.adjIterator(self.G, v)  # 找到v节点所有相邻的点，进行迭代遍历
            for i in adj:
                if not self.visited[i]:
                    q.put(i)
                    self.visited[i] = True
                    self.fromed[i] = v
                    self.ord[i] = self.ord[v] + 1

    def hasPath(self, w):
        if w >= 0 and w < self.G.V():
            return self.visited[w]

    def path(self, w):  # 从v到w的路径
        s = []
        p = w
        while p != -1:
            s.append(p)
            p = self.fromed[p]
        s.reverse()
        return s

    def showPath(self, w):
        s = self.path(w)
        if w >= 0 and w < self.G.V():
            return self.ord[w]
