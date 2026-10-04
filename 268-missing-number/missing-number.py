class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        x=(n*(n+1))//2
        sum=0
        for i in nums:
            sum+=i
        return x-sum