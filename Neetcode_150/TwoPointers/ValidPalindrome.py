"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        if len(s)==1:
            return True
        while(left<right):
            if s[left].lower().isalnum()==False:
                left+=1
                continue
            if s[right].lower().isalnum()==False:
                right-=1
                continue
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True