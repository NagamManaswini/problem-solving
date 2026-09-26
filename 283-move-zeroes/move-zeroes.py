class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=[]
        for x in range(len(nums)):
            if nums[x]!=0:
                temp.append(nums[x])
        for x in range(len(nums)):
            if nums[x]==0:
                temp.append(nums[x])
        nums[:]=temp
        return nums
        