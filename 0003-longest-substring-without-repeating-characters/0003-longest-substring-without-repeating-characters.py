class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        characters = set()
        max_length = 0

        for right in range(len(s)):

            while s[right] in characters:
                characters.remove(s[left])
                left += 1

            characters.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length        