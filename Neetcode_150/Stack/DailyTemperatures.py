"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""
#Tc= O(N) SC=O(N)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        final = [0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            if len(stack)==0:
                final[i]=0
            elif len(stack)!=0 and stack[-1][0]>temperatures[i]:
                final[i]=(stack[-1][1]-i)
            elif len(stack)!=0 and stack[-1][0]<=temperatures[i]:
                while len(stack)!=0 and stack[-1][0]<=temperatures[i]:
                    stack.pop()
                if len(stack)==0:
                    final[i]=0
                else:
                    final[i]=(stack[-1][1]-i)
            stack.append([temperatures[i],i])
        return final  
    
    #cleaner solution
    class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = len(temperatures)-1
        stack = []
        final = [-1] *len(temperatures)
        while(i>=0):
            while stack and stack[-1][0]<=temperatures[i]:
                stack.pop()
            if len(stack)==0:
                final[i]=0
            else:
                val = stack[-1][1]-i
                final[i]=val            
            stack.append([temperatures[i],i])
            i-=1
        return final