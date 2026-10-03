class Solution:
    def isPalindrome(self, x: int) -> bool:
        z=0
        y=x
        while x>0:
            z=z*10+x%10
            x//=10
        return y==z

        