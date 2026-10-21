class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    # Input: strs = ["act","pots","tops","cat","stop","hat"]

        hashmap = {}
        
        # O(m)
        for word in strs:
            arr = [0] * 26
            value = []
            
            # O(n)
            for char in word:
                arr[ord(char) - ord('a')] += 1
    
            # Convert array to tuple
            arr = tuple(arr)

            # if key isn't already in the hashmap we add it with the word appended to the list
            if arr not in hashmap:
                hashmap[arr] = []
                hashmap[arr].append(word)

            # else if it already exists then we can just append to the corresponding key
            else:
                hashmap[arr].append(word)
        
        # Return answer
        if(len(strs) <= 1):
            return([strs])

        else:
            answer = []

            for i in hashmap:
                answer.append(hashmap[i])
            
            return answer
        



        
                







   

            



            
        


        

   
                 

        