class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        start=0
        cur_sum=0
        max_freq=0
        for end in range(len(nums)):
            cur_int=nums[end]
            cur_sum+=cur_int
            while start <end and ((cur_int*(end-start+1))-cur_sum)>k:
                cur_sum-=nums[start]
                start+=1
            max_freq=max(max_freq,(end-start+1))
        return max_freq

        