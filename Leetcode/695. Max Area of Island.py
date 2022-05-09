class Solution(object):
    def check_pixel_in_2darray(self, pixel, array):
        for i in range(len(array)):
                if pixel in array[i]:
                    return True
        return False
    
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        len_row = len(grid)
        len_col = len(grid[0])
        
        all_island = []
        
        lst_add = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        for i in range(len_row):
            for j in range(len_col):
                # if grid[i][j] == 1, check whether this grid exists all_island or not
                if grid[i][j] == 1 and not self.check_pixel_in_2darray([i, j], all_island):
                    island = []
                    stack = [[i, j]]
                    # find island by BFS
                    while len(stack) > 0:
                        i_t, j_t = stack.pop()
                        island.append([i_t, j_t])
                        for x in lst_add:
                            i_tt = i_t + x[0]
                            j_tt = j_t + x[1]
                            if 0 <= i_tt < len_row and 0 <= j_tt < len_col and grid[i_tt][j_tt] == 1 and [i_tt, j_tt] not in island and [i_tt, j_tt] not in stack:
                                stack.append([i_tt, j_tt])

                    if len(island) > 0:
                        all_island.append(island)
                        
        all_area = [len(area) for area in all_island]
        if len(all_area) > 0:
            return max(all_area)
        else:
            return 0
                    
