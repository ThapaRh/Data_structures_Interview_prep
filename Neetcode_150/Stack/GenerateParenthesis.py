"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""
"""
https://leetcode.com/problems/generate-parentheses/solutions/127698/generate-parentheses/ go to this l;ink for TC and SC. Its qiite complicated
"""

"""
Time complexity is : 4^n
Here is a more detailed explanation of the space complexity:

The recur function takes two parameters: openC and close. openC is the number of open parentheses that have been used, and close is the number of close parentheses that have been used.
The function starts by checking if openC and close are both equal to n. If they are, then the function adds the current combination of parentheses to the final list and returns.
If openC is less than n, then the function adds a left parenthesis to the temp list and calls itself recursively with openC + 1 and close.
If close is less than openC, then the function adds a right parenthesis to the temp list and calls itself recursively with openC and close + 1.
When the function returns, it pops the last parenthesis from the temp list.
The stack can grow up to a depth of n because the function calls itself recursively n times. Each time the function calls itself, it pushes a new state onto the stack. The state includes the values of openC and close. When the function returns, it pops the state off of the stack.

The total space complexity of the code is O(n) because the stack can grow up to a depth of n.
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
