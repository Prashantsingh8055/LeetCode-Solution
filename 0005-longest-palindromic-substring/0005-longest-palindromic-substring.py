class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s

        # Transform string to handle odd and even length palindromes uniformly
        # e.g., "aba" -> "^#a#b#a#$"
        T = "^#" + "#".join(s) + "#$"
        n = len(T)
        P = [0] * n
        C = 0  # Center of the current rightmost palindrome
        R = 0  # Right boundary of the current rightmost palindrome

        for i in range(1, n - 1):
            i_mirror = 2 * C - i  # Mirror of i with respect to C

            if R > i:
                P[i] = min(R - i, P[i_mirror])
            else:
                P[i] = 0

            # Expand around center i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # Update center and right boundary
            if i + P[i] > R:
                C = i
                R = i + P[i]

        # Find the maximum radius and its center
        max_len = 0
        center_index = 0
        for i in range(1, n - 1):
            if P[i] > max_len:
                max_len = P[i]
                center_index = i

        # Extract the original substring
        start = (center_index - max_len) // 2
        return s[start:start + max_len]