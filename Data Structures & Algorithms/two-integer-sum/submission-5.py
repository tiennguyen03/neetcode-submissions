class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i in range(len(nums)):

            diff = target - nums[i]

            if(hashmap.get(diff) != None):
                answer = []
                answer.append(hashmap[diff])
                answer.append(i)
                return answer

            else:
                hashmap[nums[i]] = i

                
            


 





        

