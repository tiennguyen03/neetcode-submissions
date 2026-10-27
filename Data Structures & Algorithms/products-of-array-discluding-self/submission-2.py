class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Input: nums = [1,2,4,6]
        # Output: [48,24,12,8]
        output = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            output[i] *= product
            product *= nums[i]
        product = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= product
            product *= nums[j]
        return (output)


                


            

        