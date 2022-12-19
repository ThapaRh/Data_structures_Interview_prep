"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
"""

class Solution(object):
    def letterCasePermutation(self, s):
        storage_array=[]
        def casePermutation(ip,op,index): 
            while index<len(ip) and ip[index].isnumeric():
                op+=ip[index]
                index+=1
            if index==len(ip):
                storage_array.append(op)
                return
            op1 = op[:]+ip[index]
            op2 = op[:]+ip[index].swapcase()
            casePermutation(ip,op1,index+1)
            casePermutation(ip,op2,index+1)

        
        casePermutation(s,"",0)
        return storage_array