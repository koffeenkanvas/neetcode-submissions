class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(ch for ch in s if ch.isalnum())
        left = 0
        right = len(s)-1
        while left <= right:
            if s[left] == s[right]:
                left = left + 1
                right = right - 1
            else:
                return False
        return True