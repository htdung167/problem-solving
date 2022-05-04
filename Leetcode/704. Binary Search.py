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
