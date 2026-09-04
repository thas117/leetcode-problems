class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """


        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # If left, mid and right are the same,
            # we cannot know which side is sorted
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

            # Left half is sorted
            if nums[left] <= nums[mid]:

                # Target is inside left sorted half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:

                # Target is inside right sorted half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False        