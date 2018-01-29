#Leetcode120,64
#自顶向下的记忆化搜索
memo = [-1 for i in range(500+1)]
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if memo[n] == -1:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
print(fib(500))



#自底向上的动态规划
def fib1(n):
    memo = [ -1 for i in range(n+1)]
    memo[0] = 0
    memo[1] = 1
    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]
