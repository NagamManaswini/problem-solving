class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        x=set(nums1)
        y=set()
        for i in nums2:
            if i in x:
                y.add(i)
        return list(y)

        