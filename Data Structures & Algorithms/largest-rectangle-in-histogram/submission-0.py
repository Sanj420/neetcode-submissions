class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        maxa = 0
        for i,n in enumerate(heights):
            start = i
            while stk and stk[-1][1] > n:
                index, height = stk.pop()
                maxa = max(maxa, height*(i-index))
                start = index
            stk.append((start,n))
        for i,n in stk:
            maxa = max(maxa, n*(len(heights)-i))
        return maxa