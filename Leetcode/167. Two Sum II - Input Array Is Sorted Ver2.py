class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Ý tưởng: Dùng dictionary để lưu hiệu
        arr_sub = {}
        for i in range(len(numbers)):
            if numbers[i] in arr_sub.keys():
                return [arr_sub[numbers[i]] + 1, i + 1]
            else:
                arr_sub[target - numbers[i]] = i
            