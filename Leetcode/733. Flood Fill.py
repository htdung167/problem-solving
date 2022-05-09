# Ver 1
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        oldColor = image[sr][sc]
        stack = [[sr, sc]]
        len_row = len(image)
        len_col = len(image[0])

        newImage = []
        for i in range(len_row):
            arr_t = []
            for j in range(len_col):
                arr_t.append(-1)
            newImage.append(arr_t)

        while len(stack) > 0:
            pixel = stack.pop()
            sr_t, sc_t = pixel
            newImage[sr_t][sc_t] = newColor
            if sr_t - 1 >= 0 and image[sr_t - 1][sc_t] == oldColor and newImage[sr_t - 1][sc_t] == -1:
                stack.append([sr_t - 1, sc_t])
            if sc_t - 1 >= 0 and image[sr_t][sc_t - 1] == oldColor and newImage[sr_t][sc_t - 1] == -1:
                stack.append([sr_t, sc_t - 1])
            if sr_t + 1 < len_row and image[sr_t + 1][sc_t] == oldColor and newImage[sr_t + 1][sc_t] == -1:
                stack.append([sr_t + 1, sc_t])
            if sc_t + 1 < len_col and image[sr_t][sc_t + 1] == oldColor and newImage[sr_t][sc_t + 1] == -1:
                stack.append([sr_t, sc_t + 1])
        
        for i in range(len_row):
            for j in range(len_col):
                if newImage[i][j] == -1:
                    newImage[i][j] = image[i][j]
        
        return newImage
            
            
# Ver 2
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        oldColor = image[sr][sc]
        stack = [[sr, sc]]
        len_row = len(image)
        len_col = len(image[0])

        newImage = []
        for i in range(len_row):
            arr_t = []
            for j in range(len_col):
                arr_t.append(-1)
            newImage.append(arr_t)

        lst_add = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while len(stack) > 0:
            pixel = stack.pop()
            sr_t, sc_t = pixel
            newImage[sr_t][sc_t] = newColor
            for x in lst_add:
                sr_tt = sr_t + x[0]
                sc_tt = sc_t + x[1]
                if 0 <= sr_tt < len_row and 0 <= sc_tt < len_col and image[sr_tt][sc_tt] == oldColor and newImage[sr_tt][sc_tt] == -1:
                    stack.append([sr_tt, sc_tt])
            
        
        for i in range(len_row):
            for j in range(len_col):
                if newImage[i][j] == -1:
                    newImage[i][j] = image[i][j]
        
        return newImage