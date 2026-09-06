class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Use the first word as the reference
        first_word = strs[0]

        for i in range(len(first_word)):
            char = first_word[i]
            # Check if this character matches across all strings
            for other_word in strs[1:]:
                # If the current index is out of bounds or characters don't match
                if i >= len(other_word) or other_word[i] != char:
                    return first_word[:i]

        return first_word