# Ver 1
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len_s1 = len(s1)
        s1_s = sorted(list(s1))
        for i in range(len(s2) - len_s1 + 1):
            if sorted(list(s2[i:(i+len_s1)])) == s1_s:
                return True
        return False


# Ver 2
from collections import defaultdict

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        a = defaultdict(int)
        b = defaultdict(int)
        # init
        for x in s1:
            a[x] += 1
        for i in range(len(s1)):
            b[s2[i]] += 1
        for i in range(len(s1), len(s2)):
            if a == b:
                return True
            else:
                b[s2[i - len(s1)]] -= 1
                b[s2[i]] += 1
                if b[s2[i-len(s1)]] == 0:
                    del b[s2[i-len(s1)]]
        if a==b:
            return True
        return False