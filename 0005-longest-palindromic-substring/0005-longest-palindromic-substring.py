class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the valid palindrome slice indices
            return left + 1, right - 1

        start, end = 0, 0

        for i in range(len(s)):
            # Odd-length palindromes (single character center, e.g., "aba")
            l1, r1 = expand_around_center(i, i)
            if (r1 - l1) > (end - start):
                start, end = l1, r1

            # Even-length palindromes (two character center, e.g., "abba")
            l2, r2 = expand_around_center(i, i + 1)
            if (r2 - l2) > (end - start):
                start, end = l2, r2

        return s[start:end + 1]