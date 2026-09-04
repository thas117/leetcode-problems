class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        result = []

        for size in range(len(arr), 1, -1):

            # Find the position of the largest number
            max_index = arr.index(size)

            # If already in correct position, skip
            if max_index == size - 1:
                continue

            # Flip largest number to the front
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
                result.append(max_index + 1)

            # Flip it to its final position
            arr[:size] = arr[:size][::-1]
            result.append(size)

        return result        