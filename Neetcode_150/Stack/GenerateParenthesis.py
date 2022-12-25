"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""
"""
https://leetcode.com/problems/generate-parentheses/solutions/127698/generate-parentheses/ go to this l;ink for TC and SC. Its qiite complicated
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        result=[]
        openCount=0
        closedCount=0
        def backtracking(openCount,closedCount):
            if openCount==closedCount==n:
                val = "".join(stack)
                result.append(val)
                return
            if openCount<n:
                stack.append("(")
                backtracking(openCount+1,closedCount)
                stack.pop()
            if closedCount<openCount:
                stack.append(")")
                backtracking(openCount,closedCount+1)
                stack.pop()
            return
        backtracking(0,0)
        return result
