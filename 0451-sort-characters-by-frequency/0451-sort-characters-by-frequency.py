class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        count = {}

        # Count each character
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Sort characters by frequency
        characters = sorted(count, key=count.get, reverse=True)

        # Build the answer
        result = ""

        for char in characters:
            result += char * count[char]

        return result        