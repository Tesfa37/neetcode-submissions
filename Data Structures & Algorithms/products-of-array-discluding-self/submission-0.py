class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        product = [1]*len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for k in range(len(nums) - 2, -1,-1):
            postfix[k] = postfix[k+1] * nums[k+1]
        for j in range(len(nums)):
            product[j] = prefix[j] * postfix[j]
        return product