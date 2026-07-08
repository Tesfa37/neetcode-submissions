class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        if not height:
            return 0
        left, right = 0, len(height) - 1
        maxleft, maxright = height[left], height[right]
        while left < right:
            if maxleft <= maxright:
                left += 1
                maxleft = max(maxleft, height[left])
                output += maxleft - height[left]
            else:
                right -= 1
                maxright = max(maxright, height[right])
                output += maxright - height[right]
        return output