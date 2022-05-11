class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        len_row = len(mat)
        len_col = len(mat[0])
        
        q = []
        for i in range(len_row):
            for j in range(len_col):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = "#"
        
        add = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        for x, y in q:
            for i, j in add:
                add_x = x + i
                add_y = y + j
                if 0 <= add_x < len_row and 0 <= add_y < len_col and mat[add_x][add_y] == "#":
                    mat[add_x][add_y] = mat[x][y] + 1
                    q.append((add_x, add_y))
        
        return mat
            
                            
                        
                    
                    
                    