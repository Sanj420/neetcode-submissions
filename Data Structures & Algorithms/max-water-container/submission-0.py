class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mc = 0
        for i in range(len(heights)):
            for j in range(len(heights)-1, -1, -1):
                c = 0
                if heights[i]>heights[j]:
                    c+=heights[j]*(j-i)
                    mc = max(c,mc)
                elif heights[i]<heights[j]:
                    c+=heights[i]*(j-i)
                    mc = max(c,mc)
                else:
                    c+=heights[j]*(j-i)
                    mc = max(c,mc)
        return mc