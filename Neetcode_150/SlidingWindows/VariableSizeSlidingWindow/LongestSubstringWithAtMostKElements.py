"""
Given a string s and an integer k, return the length of the longest 
substring of s that contains at most k distinct characters.

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
"""

#TC=O(N) SC=O(k) because we store and delete the unnecessary stuffs

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i=0
        j=0
        dict = {}
        newString=""
        max_length=0
        while(j<len(s)):
            newString+=s[j]
            if s[j] in dict:
                dict[s[j]]+=1
            else:
                dict[s[j]]=1
            if len(dict)<=k:
                j+=1
                max_length=max(max_length,len(newString))
            else:
                while len(dict)>k:
                    dict[s[i]]-=1
                    if dict[s[i]]==0:
                        del dict[s[i]]
                    newString=newString[1:]
                    i+=1
                j+=1
        return max_length