class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        nums.sort()

        def backtrack(current, used):
            if len(current) == len(nums):
                result.append(current[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                # Skip duplicate numbers
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                current.append(nums[i])

                backtrack(current, used)

                current.pop()
                used[i] = False

        backtrack([], [False] * len(nums))

        return result       