class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        unique = sorted(set(nums))
        
        # If there are fewer than 3 distinct numbers, return the maximum
        if len(unique) < 3:
            return unique[-1]
            
        # Return the 3rd maximum from the end
        return unique[-3]

        