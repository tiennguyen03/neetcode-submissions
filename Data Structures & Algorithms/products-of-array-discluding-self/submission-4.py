class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Input : [1,2,4,6]
        # Output (Prefix): [1,1,2,8]
        # Output (Postfix): [,12,8]

        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= postfix
            postfix *= nums[j]
        

        return(output)


        