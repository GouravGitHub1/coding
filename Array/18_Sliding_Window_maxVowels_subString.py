## https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxVowelCount = 0
        currVowelCount = 0
        vowels = ['a','e','i','o','u']
        
        for i in range(k):
            if (s[i] in vowels):
                currVowelCount += 1
        
        if (currVowelCount > maxVowelCount):
            maxVowelCount = currVowelCount
        
        # print(maxVowelCount, currVowelCount)
        for i in range(k,len(s)):
            if (s[i] in vowels and k == 1):
                maxVowelCount = 1
                break
            
            # print(i - k ,i,"string",s[i - k + 1 : i+1] ,"currVowelCount",currVowelCount )
            if (s[i] in vowels):
                currVowelCount += 1
            if (s[i - k] in vowels):
                currVowelCount -= 1
                
            if (currVowelCount > maxVowelCount):
                maxVowelCount = currVowelCount
                
        return maxVowelCount
