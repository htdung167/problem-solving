# Ver 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1
        
# Ver 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target):
            left = 0
            right = len(nums) - 1
            while True:
                if right >= left:
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] > target:
                        right = mid - 1
                    else: 
                        left = mid + 1
                else:
                    return -1
        # Tìm điểm mà tại đó có giá trị không tăng 
        flag = 0
        for i in range(0, len(nums) - 1):
            if (nums[i + 1] - nums[i]) < 0:
                flag = i + 1
        search_second = binary_search(nums[flag:], target)
        if search_second != -1:
            return search_second + flag
        else:
            return binary_search(nums[:flag], target)
                
        
        