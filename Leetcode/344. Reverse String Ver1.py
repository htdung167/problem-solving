class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        ss = list(s)
        for i in range(len(s)):
            s[i] = ss[len(s) - i - 1]
        