class Solution:
    def isPalindrome(self, s: str) -> bool:
        l= 0
        r=len(s)-1
        while l<r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            left=s[l]
            right=s[r]
            if s[l].isalpha():
                left=s[l].lower()
            if s[r].isalpha():
                right=s[r].lower()
            if left==right:
                l+=1
                r-=1
            else:
                return False
        return True
        