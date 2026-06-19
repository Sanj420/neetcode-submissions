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
            if maxl<maxr:
                l+=1
                maxl = max(maxl, height[l])
                c+= maxl - height[l]
            else:
                r-=1
                maxr = max(maxr, height[r])
                c+= maxr - height[r]
               
        return c