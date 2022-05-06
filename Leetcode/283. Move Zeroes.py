class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l2r1 = 0 # So dung truoc
        l2r2 = l2r1 + 1 # So dung sau
        while(l2r2 < len(nums)):
            if nums[l2r2] == 0: # Neu so dung sau bang 0 thi tang index len 1
                l2r2 += 1
                continue
            if nums[l2r1] == 0: # Neu so dung truoc bang 0 thi hoan doi va tang index 2 so len 1
                nums[l2r1], nums[l2r2] = nums[l2r2], nums[l2r1]
                l2r1 += 1
                l2r2 += 1
            else: # Neu khong thi xay ra 2 TH duoi
                if l2r1 == l2r2 - 1:
                    l2r1 += 1
                    l2r2 += 1
                else:
                    l2r1 += 1
            
            