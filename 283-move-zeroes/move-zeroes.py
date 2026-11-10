class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        x=[]
        y=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                x.append(nums[i])

        for i in range(len(nums)):
            if nums[i]==0:
                y.append(nums[i])
        nums[:]=x+y
        return nums'''

        #two ptr approach
        count=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[count]=nums[i]
                count+=1
        for i in range(count,len(nums)):
            nums[i]=0
        return nums
            