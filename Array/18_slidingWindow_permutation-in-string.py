## https://leetcode.com/problems/permutation-in-string/submissions/


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        
        origDict = {}
        currDict = {}
        for char in s1:
            if (char in origDict.keys()):
                origDict[char] += 1
                
            else:
                origDict[char] = 1
                currDict[char] = 0
        print(origDict)
        print(currDict)

        
        
        k = len(s1)
        # # maxVowelCount = 0
        # currCount = 0
        print(k)
        for i in range(k):
            if (s2[i] in s1):
                currDict[s2[i]] += 1
            
        
        print(currDict)
        if (currDict == origDict):
            return True
        
        # print(maxVowelCount, currVowelCount)
        for i in range(k,len(s2)):
            # if (s[i] in vowels and k == 1):
            #     maxVowelCount = 1
            #     break
            
            if (s2[i] in s1):
                # currCount += 1
                currDict[s2[i]] += 1
                
            if (s2[i - k] in s1):
                # currCount -= 1
                currDict[s2[i - k]] -= 1
                
            if (currDict  == origDict):
                return True
        
        return False
