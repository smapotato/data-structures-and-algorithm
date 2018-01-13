#Leetcode79
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        global visited
        visited = [ [False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.searchWord(board,word,0,i,j):
                    return True
        return False


    def searchWord(self, board, word, index, startx, starty):
        # 从board[startx][starty]开始,寻找word[index:]
        d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        if index == len(word) - 1:  # 找到最后一个字母
            return board[startx][starty] == word[index]
        if board[startx][starty] == word[index]:
            visited[startx][starty] = True
            for i in range(4):  # 从startx，starty出发，向四个方向寻找
                newx = startx + d[i][0]
                newy = starty + d[i][1]
                if self.inArea(newx, newy, board) and not visited[newx][newy]:  # 在图形边界内并且没有访问过
                    if self.searchWord(board, word, index + 1, newx, newy):
                        return True
            visited[startx][starty] = False
        return False

    def inArea(self, x, y, board):
        return x >= 0 and x < len(board) and y >= 0 and y < len(board[0])

def exist(self, board, word):
    if not board:
        return False
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if self.dfs(board, i, j, word):
                return True
    return False

# check whether can find word, start at (i,j) position    
def dfs(self, board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian 
    # check whether can find "word" along one direction
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \\
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res
