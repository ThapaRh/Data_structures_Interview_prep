"""Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false"""

#TC= O(26.N)
#SC=O(N)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c_s1= Counter(s1)
        leng_s1=len(s1)
        i=0
        while(i+leng_s1<=len(s2)):
            new_val = s2[i:i+leng_s1]
            counter_s2=Counter(new_val)
            if c_s1==counter_s2:
                return True
            i+=1
        return False

#better and understandable
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lengths1=len(s1)
        start = 0
        end = 0
        newString = ""
        if len(s1)>len(s2):
            return False
        counters1 = Counter(s1)
        while(end<len(s2)):
            newString+=s2[end]
            if len(newString)<lengths1:
                end+=1
                continue
            while(len(newString)>lengths1):
                start+=1
                newString=newString[1:]
            counters2 = Counter(newString)
            if counters1 == counters2:
                return True
            end+=1
        return False
