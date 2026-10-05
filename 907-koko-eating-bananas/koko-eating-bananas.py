import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=0
        while low<=high:
            mid=(low+high)//2
            hours=0
            for p in piles:
                if hours<=h:
                    hours+=math.ceil(p/mid)
                else:
                    break
            if hours>h:
                low=mid+1
            else:
                high=mid-1
                ans=mid
        return ans
            



        
        