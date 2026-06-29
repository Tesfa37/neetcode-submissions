class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict_:
                return sorted([i,dict_[diff]])
            else:
                dict_[nums[i]] = i
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             if i > j:
        #                 return [j,i]
        #             else:
        #                 return [i,j]
               