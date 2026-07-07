class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Dictionary to count the frequency of each number
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Find the maximum frequency
        max_freq = max(freq.values())

        # Sum frequencies that are equal to the maximum
        total = sum(count for count in freq.values() if count == max_freq)

        return total
        