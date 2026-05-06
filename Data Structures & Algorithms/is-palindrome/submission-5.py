class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        start = 0
        back = n-1
        while start < back:
            while start<back and not self.alphaNum(s[start]):
                start+=1
            while back>start and not self.alphaNum(s[back]):
                back-=1
            if s[start].lower() != s[back].lower():
                return False
            
            start += 1
            back -= 1
        return True
    def alphaNum(self, c):
        # Function to check alpha numeric character using ascii codes
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))