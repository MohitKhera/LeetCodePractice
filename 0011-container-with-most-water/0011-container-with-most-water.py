class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_Area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            max_Area = max(max_Area, min(height[left], height[right]) * (right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_Area