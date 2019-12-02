class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l < 2:
            return s
        ans = s[0]
        maxl = 1
        for i in range(l):
            j = 0
            while i + j < l and i - j >= 0 and s[i + j] == s[i - j]:
                j += 1
            if 2 * j - 1 > maxl:
                maxl = 2 * j - 1
                ans = s[i - j + 1:i + j]
        
        for i in range(l):
            j = 0
            while i + j + 1 < l and i - j >= 0 and s[i + j + 1] == s[i - j]:
                j += 1
            if 2 * j > maxl:
                maxl = 2* j
                ans = s[i - j + 1: i + j + 1]
        return ans      
