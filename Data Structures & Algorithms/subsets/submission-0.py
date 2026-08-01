class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # to use backtracking means to choose toe include or not include element at every level
        res = []
        subset = []
        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return

            # descision to include
            subset.append(nums[i])
            dfs(i + 1)

            # desicision not to include
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res