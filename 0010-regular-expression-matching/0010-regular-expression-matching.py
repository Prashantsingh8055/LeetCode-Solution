class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        
        # dp[i][j] indicates if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns matching an empty string, like "a*", "a*b*", etc.
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Case 1: Treat '*' as 0 occurrences of the previous element
                    dp[i][j] = dp[i][j - 2]
                    
                    # Case 2: Treat '*' as 1 or more occurrences
                    # Only valid if the preceding element matches the current string character
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        return dp[m][n]