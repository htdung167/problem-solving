class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nums_t = []
        for x in nums:
            if len(nums_t) == 0 or x != nums_t[-1]:
                nums_t.append(x)
        
        print(nums_t)
        if len(nums_t) < 3 and len(list(set(nums_t))) < 3:
            return False
        for i in range(len(nums_t) - 2):
            for j in range(i + 1, len(nums_t) - 1):
                for k in range(j + 1, len(nums_t)):
                    if nums_t[i] < nums_t[k] and nums_t[k] < nums_t[j]:
                        return True
        return False
        
        
if __name__=="__main__":
    s = Solution()
    nums=[3, 1, 2, 4, 4, 2, 2]
    print(s.find132pattern(nums))