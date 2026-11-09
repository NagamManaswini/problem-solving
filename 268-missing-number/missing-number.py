class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        x=0
        y=len(nums)
        for i in range(len(nums)):
            x+=nums[i]
        z=(y*(y+1))//2
        return z-x
            


        