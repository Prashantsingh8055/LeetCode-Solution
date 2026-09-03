class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Width between the two lines
            width = right - left
            
            # Water level is constrained by the shorter line
            current_height = min(height[left], height[right])
            current_water = width * current_height
            
            if current_water > max_water:
                max_water = current_water
            
            # Move the pointer at the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water