class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        max = 0
        while start<end:
            ht = min(height[start],height[end])
            width = end-start
            area = ht * width
            if area>max:
                max = area
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return max