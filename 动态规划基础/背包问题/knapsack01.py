"""
0-1背包问题
有一个背包,它的容量为C,现有n种不同的物品,编号为0...n-1，其中每一件物品的重量为w(i)
价值为v(i),问可以向这个背包中盛放哪些物品,使得在不超过背包容量的基础上,物品的总价值
最大
F(i,c)考虑将n个物品放进容量为c的背包
F(i,c) = max(F(i-1,c),v(i)+F(i-1,c-w(i))
"""


class Solution:#记忆化搜索
    def knapsack01(self, w, v, C):
        n = len(w)
        global memo
        memo = [[-1 for i in range(C + 1)] for j in range(n)]
        return self.bestValue(w, v, n - 1, C)

    def bestValue(self, w, v, index, c):  # 用[0...index]的物品,填充容积为c的背包的最大价值
        if index < 0 and c <= 0:
            return 0
        if memo[index][c] != -1:
            return memo[index][c]
        res = self.bestValue(w, v, index - 1, c)
        if c >= w[index]:
            res = max(res, v[index] + self.bestValue(w, v, index - 1, c - w[index]))
        memo[index][c] = res
        return res

class Solution:#动态规划
    def knapsack01(self, w, v, C):
        n = len(w)
        if not n:
            return 0
        memo = [ [-1 for i in range(C+1) for j in range(n)]]
        for j in range(C+1):
            memo[0][j] = (v[0] if j >= w[o] else 0)
        for i in range(1,n):
            for j in range(C+1):
                memo[i][j] = memo[i-1][j]
                if j >= w[i]:
                    memo[i][j] = max(memo[i][j],v[i] + memo[i-1][j-w[i]])
        return memo[n-1][C]


#优化,空间复杂度0(C)
class Solution:#动态规划
    def knapsack01(self, w, v, C):
        n = len(w)
        if not n:
            return 0
        memo = [ [-1 for i in range(C+1) for j in range(2)]]#只需要两行
        for j in range(C+1):
            memo[0][j] = (v[0] if j >= w[o] else 0)
        for i in range(1,n):
            for j in range(C+1):
                memo[i%2][j] = memo[(i-1)%2][j]
                if j >= w[i]:
                    memo[i%2][j] = max(memo[i%2][j],v[i] + memo[(i-1)%2][j-w[i]])
        return memo[(n-1)%2][C]

class Solution:#动态规划
    def knapsack01(self, w, v, C):
        n = len(w)
        if not n or not C:
            return 0
        memo = [ -1 for i in range(C+1)]#只用一行
        for i in range(n):
            for j in range(C,w[i]-1,-1):
                memo[j] = max(memo[j],v[i] + memo[j-w[i]])
        return memo[C]
