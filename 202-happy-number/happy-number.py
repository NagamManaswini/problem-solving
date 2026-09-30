class Solution:
    def isHappy(self, n: int) -> bool:
        while n!=1 and n!=4:
            z=0
            while n:
                x=n%10
                z=z+x**2
                n//=10
            n=z
        if n==1:
            return True
        else:
            return False
        