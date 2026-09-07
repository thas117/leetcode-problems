class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)

        dp = [[0] * n for _ in range(n)]

        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        # Check substrings from shorter to longer
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1] if length > 2 else 2

                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]        