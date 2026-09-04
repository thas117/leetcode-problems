class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """


        # Count frequency of each number
        count = {}

        for num in arr1:
            count[num] = count.get(num, 0) + 1

        result = []

        # Add numbers according to arr2 order
        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]

        # Add remaining numbers in ascending order
        remaining = []

        for num in count:
            remaining.append(num)

        remaining.sort()

        for num in remaining:
            result.extend([num] * count[num])

        return result        