# Ver 1
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lstt = []
        for lst in matrix:
            lstt = [*lstt, *lst]
        left = 0
        right = len(lstt) - 1
        while True:
            if right >= left:
                mid = (left + right) // 2
                if lstt[mid] == target:
                    return True
                elif lstt[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                return False

# Ver 2
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lstt = []
        for lst in matrix:
            lstt = [*lstt, *lst]
        print(lstt)
        try:
            lstt.index(target) 
            return True
        except:
            return False
        