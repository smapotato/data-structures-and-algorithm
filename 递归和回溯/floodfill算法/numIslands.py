#Leetcode200,130,417
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        global visited
        visited = [ [False for j in range(len(grid[0]))] for i in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    self.dfs(grid,i,j)
        return res
    def dfs(self,grid,x,y):#从grid[x][y]，进行floodfill
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        visited[x][y] = True
        for i in range(4):
            newx = x + d[i][0]
            newy = y + d[i][1]
            if self.inArea(newx,newy,grid) and not visited[newx][newy] and grid[newx][newy] == "1":
                self.dfs(grid,newx,newy)
        return True

    def inArea(self, x, y, grid):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])
