class ReadGraph(object):
    """读取文件中的图"""
    def __init__(self, graph, filename):
        with open(filename, 'r') as f:
            line = f.readline()
            v, e = self.stringstream(line)
            if v == graph.V():
                lines = f.readlines()
                for i in lines:
                    a,b = self.stringstream(i)
                    if a >= 0 and a < v and b >=0 and b < v:
                        graph.addEdge(a, b)

    def stringstream(self, text):
        result = text.strip('\n')
        result = result.split()
        a, b = result
        return int(a), int(b)
