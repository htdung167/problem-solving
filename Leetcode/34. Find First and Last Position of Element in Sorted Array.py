class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while True:
            if right >= left:
                mid = (right + left) // 2
                if nums[mid] == target:
                    while (mid - 1 >= 0 and nums[mid - 1] == target):
                        mid = mid - 1
                    x = mid
                    while (x + 1 < len(nums) and nums[x+1] == target):
                        x = x + 1
                    return [mid, x]
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                return [-1, -1]
        