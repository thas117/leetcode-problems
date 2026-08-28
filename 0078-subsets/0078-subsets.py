class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        def backtrack(i, current):
            if i == len(nums):
                result.append(current[:])
                return

            # Don't take nums[i]
            backtrack(i + 1, current)

            # Take nums[i]
            current.append(nums[i])
            backtrack(i + 1, current)

            # Remove it for the next choice
            current.pop()

        backtrack(0, [])

        return result        