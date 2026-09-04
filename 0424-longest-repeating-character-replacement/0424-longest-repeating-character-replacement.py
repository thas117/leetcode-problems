class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        count = {}

        left = 0
        max_frequency = 0
        answer = 0

        for right in range(len(s)):

            # Count the current character
            count[s[right]] = count.get(s[right], 0) + 1

            # Maximum frequency in the window
            max_frequency = max(max_frequency, count[s[right]])

            # Number of characters we need to replace
            window_size = right - left + 1
            characters_to_change = window_size - max_frequency

            # If too many replacements are needed,
            # move left forward
            while characters_to_change > k:
                count[s[left]] -= 1
                left += 1

                window_size = right - left + 1
                characters_to_change = window_size - max_frequency

            # Save the largest valid window
            answer = max(answer, right - left + 1)

        return answer        