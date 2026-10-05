class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=0
        max_sum=nums[0]
        for i in nums:
            if current_sum<0:
                current_sum=0
            current_sum+=i
            max_sum=max(max_sum,current_sum)
        return max_sum




























        '''
        res = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0

            total += n
            res = max(res, total)
        
        return res
'''
    