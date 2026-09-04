class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)

        duplicate = 0
        missing = 0

        # Find duplicate
        for num in nums:
            if nums.count(num) == 2:
                duplicate = num
                break

        # Find missing
        for i in range(1, n + 1):
            if i not in nums:
                missing = i
                break

        return [duplicate, missing]        