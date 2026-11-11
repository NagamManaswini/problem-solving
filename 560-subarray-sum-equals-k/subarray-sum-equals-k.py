class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        subsum=0
        freq={0:1}
        for i in nums:
            subsum+=i
            if subsum-k in freq:
                count+=freq[subsum-k]
            if subsum in freq:
                freq[subsum]+=1
            else:
                freq[subsum]=1
        return count

        