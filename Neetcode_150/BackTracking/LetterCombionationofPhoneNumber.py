"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []"""
#TC= O(4^n) SC= O(4)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict={
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
            }
        count=len(digits)
        res=[]
        def DFS(i,op):
            if len(op)==len(digits):
                res.append(op)
                return
            for c in dict[digits[i]]:
                DFS(i+1,op+c)
        if digits:
            DFS(0,"")
            return res
        else:
            return res
