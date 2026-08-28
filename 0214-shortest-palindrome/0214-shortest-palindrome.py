class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        rev = s[::-1]

        temp = s + "#" + rev

        lps = [0] * len(temp)

        i = 1
        length = 0

        while i < len(temp):
            if temp[i] == temp[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    i += 1

        longest = lps[-1]

        return rev[:len(s) - longest] + s        