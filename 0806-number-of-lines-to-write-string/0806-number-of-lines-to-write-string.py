class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """

        lines = 1
        current = 0

        for ch in s:
            width = widths[ord(ch) - ord('a')]

            if current + width > 100:
                lines += 1
                current = width
            else:
                current += width

        return [lines, current]       