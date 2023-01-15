"""Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb""""
#Tc = O(n^2) SC = O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        i=0
        longestPalindrome=""
        lengthLongest = 0
        while(i<len(s)):
            j=i
            while(j+1<len(s) and s[j]==s[j+1]): #checking to see if the letters are same like aaaa
                j+=1
            left = i
            right = j
            while (left>=0 and right<len(s) and s[left]==s[right]): #checking to see if value from left and right of chosen character is equal, if equal palindrome, else continue
                length = right-left+1 
                if length>lengthLongest:
                    lengthLongest=length
                    longestPalindrome = s[left:right+1]
                left-=1
                right+=1
            i=j+1
        return longestPalindrome
        