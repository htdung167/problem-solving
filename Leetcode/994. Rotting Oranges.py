class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        len_row = len(grid)
        len_col = len(grid[0])
        
        rotten_oranges = []
        
        rotten_orange = []
        
        for i in range(len_row):
            for j in range(len_col):
                if grid[i][j] == 2:
                    rotten_orange.append((i, j))
        
        rotten_oranges.append(rotten_orange)
        
        
        add = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while len(rotten_oranges[-1]) > 0:
            stack = rotten_oranges[-1].copy()
            rotten_orange = []
            while len(stack) > 0:
                x_orange, y_orange = stack.pop(0)
                for m, n in add:
                    xx_orange = x_orange + m
                    yy_orange = y_orange + n
                    if 0 <= xx_orange < len_row and 0 <= yy_orange < len_col and grid[xx_orange][yy_orange]==1 and (xx_orange, yy_orange) not in stack:
                        rotten_orange.append((xx_orange, yy_orange))
                        grid[xx_orange][yy_orange] = 2 
            rotten_oranges.append(rotten_orange)
        
        
        
        
        for i in range(len_row):
            for j in range(len_col):
                if grid[i][j] == 1:
                    return -1
        if len(rotten_oranges) == 1 and len(rotten_oranges[0]) == 0:
            return 0
        
        
        return len(rotten_oranges) - 2
                    
            
        
        