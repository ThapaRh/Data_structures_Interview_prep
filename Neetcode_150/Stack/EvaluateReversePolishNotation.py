"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
"""
#Tc=O(N) SC=O(N)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            value = float('inf')-1
            try:
                value = int(tokens[i])
            except:
                value=float('inf')-1
            if value!=float('inf')-1:
                stack.append(int(tokens[i]))
            else:
                if len(stack)>=2:
                    a= stack.pop()
                    b=stack.pop()
                    if tokens[i]=="*":
                        curr=a*b
                        stack.append(curr)
                    elif tokens[i]=="/":
                        curr=int(b/a)

                        stack.append(curr)
                    elif tokens[i]=="+":
                        curr=b+a
                        stack.append(curr)
                    elif tokens[i]=="-":
                        curr=b-a
                        stack.append(curr)
        return stack.pop()



def evalRPN(self, tokens):
    
    stack = []
    
    for token in tokens:
        
        if token not in "+-/*":
            stack.append(int(token))
            continue
    
        number_2 = stack.pop()
        number_1 = stack.pop()
        
        result = 0
        if token == "+":
            result = number_1 + number_2
        elif token == "-":
            result = number_1 - number_2
        elif token == "*":
            result = number_1 * number_2
        else:
            result = int(number_1 / number_2)
            
        stack.append(result)

    return stack.pop()