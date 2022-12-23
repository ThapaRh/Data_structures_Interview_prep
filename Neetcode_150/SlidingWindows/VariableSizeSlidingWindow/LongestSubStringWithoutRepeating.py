"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
#Tc=O(N) SC=O(k)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_unique=set()
        i=0
        j=0
        substring=""
        maxLength=0
        while(j<len(s)):
            if s[j] not in sub_unique:
                substring+=s[j]
                sub_unique.add(s[j])
                length= (j-i)+1
                maxLength=max(maxLength,length)
                j+=1
            else:
                while s[j] in sub_unique:
                    sub_unique.remove(s[i])
                    substring=substring[1:]
                    i+=1
        return maxLength

