class UnionFind():
    def __init__(self, count):
        self.count = count
        self.rank = [1 for _ in range(count)]
        self.parent = [x for x in range(count)]

    def find(self, p):
        if p >= 0 and p < self.count:
            while p != self.parent[p]:
                self.parent[p] = self.parent[self.parent[p]]
                p = self.parent[p]
            return p
        else:
            return "Error"

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def Union(self, p, q):
        proot, qroot = self.find(p), self.find(q)
        if proot == qroot:
            pass
        if self.rank[proot] < self.rank[qroot]:
            self.parent[proot] = qroot
        elif self.rank[proot] > self.rank[qroot]:
            self.parent[qroot] = proot
        else:
            self.parent[proot] = qroot
            self.rank[qroot] += 1
