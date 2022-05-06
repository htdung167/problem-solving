class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Ý tưởng: lấy hiệu target - số đầu, dùng binary search tìm hiệu đó trong chuỗi còn lại
        for i in range(len(numbers) - 1):
            sub = target - numbers[i]
            left = i + 1
            right = len(numbers) - 1
            while(right >= left):
                mid = (left + right) // 2
                if numbers[mid] == sub:
                    return [i + 1, mid + 1]
                elif numbers[mid] < sub:
                    left = mid + 1
                else:
                    right = mid - 1
            