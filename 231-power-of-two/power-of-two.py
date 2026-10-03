
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n&(n-1)==0)#here ex:8>0 and 8&7 this & operator compares bits ,so power of 2 has always one '1' present
    
        
        