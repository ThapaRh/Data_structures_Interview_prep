"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

#TC: O(N klogk) n is length of given array and k is the length of longest string
#SC= O(N K) 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in range(len(strs)):
            new_word="".join(sorted(strs[i]))
            if new_word in dict:
                dict[new_word].append(strs[i])
            else:
                dict[new_word]=[strs[i]]
        return dict.values()
