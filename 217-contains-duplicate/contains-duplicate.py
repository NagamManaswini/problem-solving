class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq={}
        '''for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in freq:
            if freq[i]>1:
                return True
        return False'''
        for i in nums:
                freq[i]=freq.get(i,0)+1
        for i in freq:
            if freq[i]>1:
                return True
        
        return False