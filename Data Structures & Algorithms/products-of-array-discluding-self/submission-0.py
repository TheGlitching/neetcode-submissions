class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        product_so_far = 1
        for i in range(len(nums)):
            output[i] = product_so_far
            product_so_far *= nums[i]
        
        product_so_far = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= product_so_far
            product_so_far *= nums[i]
        
        return output