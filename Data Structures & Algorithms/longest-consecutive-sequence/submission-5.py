class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Removes Duplicates and Created a Hashset
        hashmap = set(nums)
        longest_streak = 0

        for num in hashmap:
            if num - 1 not in hashmap:
                current_streak = 1

                while(num + current_streak) in hashmap:
                    current_streak += 1

            
                longest_streak = max(longest_streak,current_streak)

        return(longest_streak)







        