class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while(l < r):

            print(f'Left: {l}, Right: {r}')
            print(f'Left Char: {s[l]}, Right Char: {s[r]}')

            if((s[l].lower()).isalnum() == False):
                l += 1
                continue

            if(((s[r].lower()).isalnum()) == False):
                r -= 1
                continue

            if(s[l].lower() != s[r].lower()):
                return False

            l += 1
            r -= 1
        
        return True
        