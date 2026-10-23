class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = [] 

        for word in strs:
            word_length = 0

            for letter in word:
                word_length += 1

            print(f'Length of Word "{word}" : {word_length}')

            encoded_string.append(str(word_length) + "#" + word)

        print(encoded_string)

        encoded_string = "".join(encoded_string)

        print(encoded_string)

        return(encoded_string)

        
    def decode(self, s: str) -> List[str]:

        decoded_string = []

        i = 0
        count = ''

        while i < len(s):
            if(s[i] == '#'):
                decoded_string.append(s[i + 1: i + 1 + int(count)])
                i = i + 1 + int(count)
                count = ''
            else:
                count += s[i]
                i += 1

        
        print(decoded_string)
        return decoded_string
