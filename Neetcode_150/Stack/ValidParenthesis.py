"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
#Tc=O(N) SC=O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        dict_b = {")":"(","]":"[","}":"{"}
        b_stack = []
        for brackets in s:
            if brackets in dict_b:
                if len(b_stack) == 0:
                    return False
                else:
                    if b_stack.pop()!=dict_b[brackets]:
                        return False
            else:
                b_stack.append(brackets)
        if len(b_stack)==0:
            return True
        return False