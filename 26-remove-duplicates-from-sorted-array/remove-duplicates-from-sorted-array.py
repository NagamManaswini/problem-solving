class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=len(nums)
        if x<=1:
            return x
        k=1
        for i in range(len(nums)):
            if nums[i]!=nums[k-1]:
                nums[k]=nums[i]
                k+=1
           
        return k