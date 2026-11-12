class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split()
        low=0
        high=len(x)-1
        while low<high:
            x[low],x[high]=x[high],x[low]
            low+=1
            high-=1
        return " ".join(x)
        