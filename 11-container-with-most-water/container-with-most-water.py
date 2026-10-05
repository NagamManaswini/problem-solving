class Solution:
    def maxArea(self, height: list[int]) -> int:
        '''
        ma=0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                h=min(height[i],height[j])
                b=j-i
                area=h*b
                ma=max(ma,area)
        return ma'''
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            width=right-left
            current_area=min(height[left],height[right])*width
            max_area=max(max_area,current_area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area


        