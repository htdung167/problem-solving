class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Ý tưởng: nếu tổng lớn hơn target thì right - 1, nếu tổng bé hơn target thì left - 1
        left = 0
        right = len(numbers) - 1
        
        while right >= left:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
            