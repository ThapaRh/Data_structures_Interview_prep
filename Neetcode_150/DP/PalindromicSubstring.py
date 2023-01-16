"""Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa"."""
#TC=O(n^2) SC=O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        # palin = []
        count=0
        for i in range(len(s)):
            start=i
            end=i
            while(start>=0 and end<len(s) and s[start]==s[end]):
                # palin.append(s[start:end+1])
                count+=1
                start-=1
                end+=1
            start=i
            end=i+1
            while(start>=0 and end<len(s) and s[start]==s[end]):
                # palin.append(s[start:end+1])
                count+=1
                start-=1
                end+=1
        return count


