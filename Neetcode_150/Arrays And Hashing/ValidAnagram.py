"""

242. Valid Anagram
Easy
7.7K
250
company
Bloomberg
company
Amazon
company
Apple
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

"""

#There is two ways to do this: by sorting TC= nlog(n) SC: O(1)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        print(sorted(s))
        if sorted(s)==sorted(t):
            return True
        return False


# By using hastable: TC: O(n) and SC:O(n)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict= {}
        if len(s)!=len(t):
            return False
        for letters in s:
            if letters in dict:
                dict[letters]+=1
            else:
                dict[letters]=1
        for letters in t:
            if letters not in dict:
                return False
            else:
                if dict[letters]==0:
                    return False
                dict[letters]-=1
        return True