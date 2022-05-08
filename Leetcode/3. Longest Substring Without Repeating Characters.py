# Ver 1

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_substr = 0
        for i in range(len(s)):
            lst_char = []
            for j in range(i, len(s)):
                if s[j] not in lst_char:
                    lst_char.append(s[j])
                else:
                    break
            if len(lst_char) > max_substr:
                        max_substr = len(lst_char)
        return max_substr
                

# Ver 2
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_substr = 0
        i = 0
        while i < len(s):
            lst_char = []
            j = i
            while j < len(s):
                if s[j] not in lst_char:
                    lst_char.append(s[j])
                else:
                    i = lst_char.index(s[j]) + i
                    break
                j += 1
                
            if len(lst_char) > max_substr:
                max_substr = len(lst_char)
            i += 1
                    
            
        return max_substr
                
            
        
            
        