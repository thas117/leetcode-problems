class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        # Step 1: Ignore numbers that are not useful
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Step 2: Mark numbers that exist
        for num in nums:
            value = abs(num)

            if value <= n:
                nums[value - 1] = -abs(nums[value - 1])

        # Step 3: Find the first positive position
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1        