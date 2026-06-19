class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl = maxr = 0
        water = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= maxl:
                    maxl = height[l]
                else:
                    water += maxl - height[l]
                l += 1
            else:
                if height[r] >= maxr:
                    maxr = height[r]
                else:
                    water += maxr - height[r]
                r -= 1
        return water