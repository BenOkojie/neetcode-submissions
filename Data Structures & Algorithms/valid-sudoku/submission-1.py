class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            
            col={}
            row={}
            
            for j in range(len(board)):
                
                if board[i][j] in col:
                    print("row")
                    return False
                else:
                    if board[i][j]!=".":
                        col[board[i][j]]=1
                if board[j][i] in row:
                    print("col")
                    return False
                else:
                    if board[j][i]!=".":
                        row[board[j][i]]=1
        for i in range(len(board)):
            grid = {}
            print(grid)
            for y in range(3):
                yindex = y
                if i%3 == 0:
                    yindex+=i
                for x in range(3):
                    xindex = x+(3*(i%3))
                    print("x: " + str(xindex) +" y: " + str(yindex))
                    if board[yindex][xindex] in grid:
                        print(grid)
                        return False
                    else:
                        if board[yindex][xindex]!=".":
                            grid[board[yindex][xindex]]=1
            print(grid)
                
        return True
