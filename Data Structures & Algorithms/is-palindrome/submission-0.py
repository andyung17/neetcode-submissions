class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.lower()

        sentence = ""

        # Handle alphanumeric and tolower
        for letter in s:
            if letter.isalnum() == False:
                letter = ""
            sentence += letter.lower()

        for i in range(len(sentence) // 2):
            if sentence[i] != sentence[len(sentence) - 1 - i]:
                return False
        
        return True