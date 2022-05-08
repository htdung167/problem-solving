# Ver 1

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except:
            return -1


if __name__ == "__main__":
    arr = [-1, 0, 3, 5, 9, 12]
    tar = 9
    s = Solution()
    print(s.search(arr, tar))



# Ver 2

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1
        while True:
            if right >= left:
                mid = (right + left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                return -1


if __name__ == "__main__":
    arr = [5]
    tar = 5
    s = Solution()
    print(s.search(arr, tar))
