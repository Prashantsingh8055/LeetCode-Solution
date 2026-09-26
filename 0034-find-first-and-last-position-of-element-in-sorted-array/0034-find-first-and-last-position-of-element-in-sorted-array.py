class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_bound(is_first):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        # Continue searching on the left side
                        right = mid - 1
                    else:
                        # Continue searching on the right side
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        start = find_bound(is_first=True)
        # If target isn't found at all, early exit
        if start == -1:
            return [-1, -1]
        
        end = find_bound(is_first=False)
        return [start, end]