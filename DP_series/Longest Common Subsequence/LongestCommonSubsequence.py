"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
"""

#Dp : base condition
    #Choice Diagram
    #Smaller Input
#For base condition : think of smallest valid input 

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        len1=len(text1)
        len2=len(text2)
        dict={}
        def recur(text1,text2,len1,len2):
            if len1==0 or len2==0:
                return 0
            if (len1,len2) in dict:
                return dict[(len1,len2)]
            if text1[len1-1]==text2[len2-1]:
                dict[(len1,len2)] = 1+ recur(text1,text2,len1-1,len2-1)
                return dict[(len1,len2)]
            else:
                dict[(len1,len2)] = max(recur(text1,text2,len1,len2-1), recur(text1,text2,len1-1,len2))
                return dict[(len1,len2)]
        return recur(text1,text2,len1,len2)