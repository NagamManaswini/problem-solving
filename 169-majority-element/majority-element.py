class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        max=0
        maj=0
        for i in freq:
            if freq[i]>max:
                max=freq[i]
                maj=i
        return maj
