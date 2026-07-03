class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums)
        maxcount = 0
        for num in new:
            if (num - 1) not in new:
                count = 0
                while (num + count) in new:
                    count += 1
                maxcount = max(maxcount, count)
        return maxcount