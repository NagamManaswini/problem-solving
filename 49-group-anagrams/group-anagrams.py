class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq={}
        for i in strs:
            sorted_word=" ".join(sorted(i))
            if sorted_word not in freq:
                freq[sorted_word]=[]
            freq[sorted_word].append(i)
        return list(freq.values())
    

        