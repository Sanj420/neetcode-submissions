class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        maxl = height[l]
        maxr = height[r]
        c= 0
        while l<r:
            if height[l]<=height[r]:
                maxl = max(maxl, height[l])
                c+= maxl - height[l]
                l+=1
            else:
                maxr = max(maxr, height[r])
                c+= maxr - height[r]
                r-=1
        return c