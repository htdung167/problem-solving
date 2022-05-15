class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # VD: n = 4, k = 2
        # Khoi tao: sample = [1, 2]
        # result = [[1, 2]], stack = [[1, 2]], arr_t = [1, 3]
        # result = [[1, 2], [1, 3]], stack = [[1, 3]], arr_t = [2, 3], arr_t = [1, 4]
        # result = [[1, 2], [1, 3], [2, 3], [1, 4]], stack = [[2, 3], [1, 4]], arr_t = [2, 4]
        # result = [[1, 2], [1, 3], [2, 3], [1, 4], [2, 4]], stack = [[2, 3], [2, 4]], arr_t = [3, 4]
        # result = [[1, 2], [1, 3], [2, 3], [1, 4], [2, 4], [3, 4]], stack = [[2, 3], [3, 4]], arr_t = empty
        # result = [[1, 2], [1, 3], [2, 3], [1, 4], [2, 4], [3, 4]], stack = [[2, 3]], arr_t = [2, 4]
        # result = [[1, 2], [1, 3], [2, 3], [1, 4], [2, 4], [3, 4]], stack = [], arr_t = empty

        sample = [i for i in range(1, k + 1)]
        result = [sample]
        stack = [sample]
        while len(stack) > 0:
            arr = stack.pop()
            for i, x in enumerate(arr):
                if i == len(arr) - 1:
                    if x < n:
                        arr_t = [*arr[:i], x+1]
                        if arr_t not in result:
                            stack.append(arr_t)
                            result.append(arr_t)
                else:
                    if x + 1 < arr[i+1]:
                        arr_t = [*arr[:i], x+1, *arr[i+1:]]
                        if arr_t not in result:
                            stack.append(arr_t)
                            result.append(arr_t)
        return result
                        
                        
                            
        
        
        