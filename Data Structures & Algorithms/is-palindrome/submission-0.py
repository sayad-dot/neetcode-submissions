class Solution:
    def isPalindrome(self, s):
        clean=""
        for ch in s:
            if ch.isalnum():
                clean +=ch.lower()
        s2 = clean[::-1]

        if clean == s2:
            return True

        return False