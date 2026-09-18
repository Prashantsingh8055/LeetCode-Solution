class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # k points to the index of the last placed unique element
        k = 0
        
        for i in range(1, len(nums)):
            # Whenever a new unique element is found, place it at k + 1
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
                
        # Total number of unique elements is k + 1
        return k + 1