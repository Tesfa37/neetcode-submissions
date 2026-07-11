class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """ Given: input: nums = [int], k = int and sliding window of size k
        return [] - max element in the window at each step
        keep track of the maximum element
        start by iterating through the list until we have the intended size for the window
        once we do then we will add the max in the max list. """
        left = 0
        right = left + k
        output = []
        maximum = 0
        while right <= len(nums):
            maximum = max(nums[left:right])
            output.append(maximum)
            left += 1
            right += 1
        return output