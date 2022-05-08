# Ver 1
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

# Ver 2
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
            

# Ver 3
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
            