
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = [0] * len(nums)
        count = 0
        freq = {0: 1}

        for i in range(len(nums)):
            if i == 0:
                prefixsum[i] = nums[i]
            else:
                prefixsum[i] = prefixsum[i-1] + nums[i]

            if prefixsum[i]-k in freq:
                count += freq[prefixsum[i]-k]

            if prefixsum[i] in freq:
                freq[prefixsum[i]] += 1
            else:
                freq[prefixsum[i]] = 1

        return count
