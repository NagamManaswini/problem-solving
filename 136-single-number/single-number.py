class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        x=nums[0]
        for i in range(1,len(nums)):
            x=x^nums[i]
        return x'''
        x={}
        for i in nums:
            if i not in x:
                x[i]=1
            else:
                x[i]+=1
        for i in x:
            if x[i]==1:
                return i