class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n={}
        for i in nums:
            if i not in n:
                n[i]=1
            else:
                n[i]+=1
        for i in n:
            if n[i]>1:
                return i
        