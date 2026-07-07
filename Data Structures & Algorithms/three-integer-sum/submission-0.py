class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        solution = []
        for i in range(len(nums_sorted)-2):
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue
            j = i +1
            k = len(nums) - 1
            while j < k:
                if nums_sorted[j] + nums_sorted[k] > -nums_sorted[i]:
                    k -= 1
                elif nums_sorted[j] + nums_sorted[k] < -nums_sorted[i]:
                    j += 1
                else:
                    solution.append([nums_sorted[i], nums_sorted[j], nums_sorted[k]])
                    j += 1
                    k -= 1
                    while j < k and nums_sorted[j] == nums_sorted[j-1]:
                        j += 1
                
        return solution