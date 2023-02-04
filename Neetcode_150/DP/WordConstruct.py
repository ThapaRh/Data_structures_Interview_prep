"""Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word."""

#m=length of word
#n=length of array
#Tc=O(n*m)

#SC= O(m*n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dict = {}
        def wordFind(s,wordDict):
            if s in dict:
                return dict[s]
            if len(s)==0:
                return True
            for word in wordDict:
                if s.find(word)==0:
                    newWord = s[len(word):]
                    print(newWord)
                    dict[s]= wordFind(newWord,wordDict)
                    if dict[s]==True:
                        return True
            dict[s]=False
            return dict[s]
        return wordFind(s,wordDict)