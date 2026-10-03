class Solution:
    def isHappy(self, n: int) -> bool:
        while n!=1 and n!=4:
            sum=0
            x=0
            while n:
                sum=n%10
                x+=sum**2
                n//=10
            n=x
        if n==1:
            return True
        else:
            return False

    