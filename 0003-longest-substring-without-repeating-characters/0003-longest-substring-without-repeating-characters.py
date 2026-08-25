class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            # If the character is already in the current window, move the left pointer
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            # Update the latest index of the character
            char_index[char] = right
            
            # Calculate window length
            max_length = max(max_length, right - left + 1)

        return max_length