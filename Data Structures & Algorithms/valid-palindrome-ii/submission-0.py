class Solution:
    def validPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]
            l += 1
            r -= 1
        return True

        # def isPalindrome(i, j):
        #     while i < j:
        #         if s[i] != s[j]:
        #             return False
        #         i += 1
        #         j -= 1
        #     return True
        # left, right = 0, len(s) - 1
        # while left < right:
        #     if s[left] == s[right]:
        #         left += 1
        #         right -= 1
        #     else:
        #         return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
        # return True
