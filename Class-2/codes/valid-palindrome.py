class Solution:
    def isPalindrome(self, s):
        m = ''.join(filter(str.isalnum, s)).lower()
        start = 0
        end = len(m) - 1
        while start < end:
            if m[start] != m[end]:
                return False
            start += 1
            end -= 1
        return True
