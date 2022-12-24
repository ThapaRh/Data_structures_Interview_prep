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
        if len(s)==1:
            return False
        stack=[]
        for b in s:
            if b=="(" or b=="[" or b=="{":
                stack.append(b)
            else:
                if len(stack)==0:
                    return False
                else:
                    val=stack.pop()
                    if (b==")" and val!="(") or (b=="]" and val!="[") or  (b=="}" and val!="{"):
                        return False
        if len(stack)==0:
            return True
        return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"}":"{", "]":"[",")":"("}
        for paren in s:
            if paren=="{" or paren == "(" or paren == "[":
                stack.append(paren)
            else:
                if len(stack)==0:
                    return False
                elif dict[paren]!=stack.pop():
                        return False
        if len(stack)==0:
            return True
        else:
            return False