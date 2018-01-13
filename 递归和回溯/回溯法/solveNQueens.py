#Leetcode51,52,37
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        global res,dia1,dia2,col
        res = []
        col = [ False for i in range(n)]#标记已经用过的列
        dia1 = [ False for i in range(2*n-1)]#对角线，左下右上对角线上的和均为横纵坐标之和，有2n-1个
        dia2 = [ False for i in range(2*n-1)]#左上右下对角线的i-j+n-1
        self.putQueen(n,0,[])
        return res
    def putQueen(self,n,index,row):#尝试在一个n皇后问题中，摆放第index行的皇后位置
        if index == n:
            res.append(self.generateBoard(n,row))
            return res
        for i in range(n):#尝试将第index行的皇后摆放在第i列
            if not col[i] and not dia1[index+i] and not dia2[index-i+n-1]:
                row.append(i)
                col[i] = True
                dia1[index+i] = True
                dia2[index-i+n-1] = True
                self.putQueen(n,index+1,row)
                col[i] = False
                dia1[index+i] = False
                dia2[index-i+n-1] = False
                row.pop()
        return True
    def generateBoard(self,n,row):
        board = ["."* n for j in range(n)]
        for i in range(n):
            board[i] = board[i][:row[i]] + "Q" + board[i][row[i]+1:]
        return board
