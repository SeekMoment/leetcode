class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        h1 = 0
        for h in height:
            h1 = max(h1, h)
            water += h1 - h
        h2 = 0
        for h in height[::-1]:
            h2 = max(h2, h)
            water -= h1 - h2
        return water
