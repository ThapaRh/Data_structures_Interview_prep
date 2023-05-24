"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

TC=O(n)
Sc=O(N)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        end = 0
        dictt={}
        if len(t)==0 or len(t)>len(s):
            return ""
        for letters in t:
            dictt[letters] = 1 + dictt.get(letters,0)
        
        dict2={}
        have = 0
        need = len(t)
        min_length = float("infinity")
        res = []
        resLength = 0
        while(end<len(s)):
            c= s[end]
            dict2[s[end]] = 1 + dict2.get(s[end],0)
            if c in dictt and dict2[c]<=dictt[c]:
                have+=1
            while(have==need):
                if end-start+1 < min_length:
                    min_length = min( min_length, end-start+1)
                    res = [start, end]
                dict2[s[start]]-=1
                if s[start] in dictt and dict2[s[start]]<dictt[s[start]]:
                    have-=1
                start+=1
            end+=1
        if min_length<float("infinity"):
            return s[res[0]:res[1]+1]
        else:
            return ""