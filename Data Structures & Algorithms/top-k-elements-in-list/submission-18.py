class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        buckets = [[] for _ in range(len(nums))]

        for n in nums:
            if n not in hashmap:
                hashmap.setdefault(n, 1)
            else:
                hashmap[n] += 1

        # Edge Case 
        if(len(hashmap) == 1):
            return(list(hashmap))
            

        # index = frequency
        # value that occured of that frequency into the buck
        for i in hashmap:
            buckets[hashmap[i]].append(i)

        j = len(nums) - 1
        # k will be our counter here

        answer = []

        while(k > 0):

            # We skip empty slots
            if(buckets[j] == []):
                j -= 1
            else:
                answer.extend(buckets[j])
                k -= len(buckets[j])
                j -= 1
 
        return(answer) 
        