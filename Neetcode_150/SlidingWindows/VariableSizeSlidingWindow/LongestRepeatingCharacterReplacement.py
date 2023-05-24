"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
"""

'''
Solution Approach: 
my thought process: 
1. put the letters in dictionary with count 
2. now use max_freq to store the count of charatcter that is most occuring
3. make sure to use two pointers, start pointer that stays in the front only moves when the window size is large and second pointer for iterating over string. Say, j,i
4. now we will check to see if i-j+1-max_freq is less than k
5. if it is then we move the window by 1, like j+=1 and delete count from dict : dict[s[j]]-=1 
6. if not then we calculate the length of that substring i-j+1 and we will store it in global variable max_length like: max_length = max(max_length, i-j+1)

'''
#TC=O(n) SC=O(m) mmm unique characters
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=0
        dict={}
        max_freq=0
        longest_substring=0
        while(j<len(s)):
            if s[j] in dict:
                dict[s[j]]+=1
            else:
                dict[s[j]]=1
            max_freq = max(max_freq,dict[s[j]])

            length_of_substring = (j-i + 1)
            valid_length = length_of_substring - max_freq
            if valid_length>k:
                dict[s[i]]-=1
                i+=1
            longest_substring = j-i+1
            j+=1
        return longest_substring