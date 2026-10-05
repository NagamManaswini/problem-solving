class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        '''
        ma=0
        x=len(nums)
        for i in range(x-k+1):
            sum=0
            for j in range(i,i+k):
                sum=sum+nums[j]
            a=sum/k
            ma=max(a,ma)
        return ma'''
        current_sum=sum(nums[:k])
        max_sum=current_sum
        for i in range(k,len(nums)):
            current_sum+=nums[i]-nums[i-k]
            if current_sum>max_sum:
                max_sum=current_sum
        return max_sum/k
        