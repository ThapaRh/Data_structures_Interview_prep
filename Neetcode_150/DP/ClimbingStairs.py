"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step"""
#TC=O(n) because of memoization SC=O(N) 

class Solution:
    def climbStairs(self, n: int) -> int:
      ##recursion with memoization:
        dict={}
        def climb(n):
            if n==1:
                return 1
            if n==2:
                return 2
            if n<1:
                return 0
            if n in dict:
                return dict[n]
            dict[n] = climb(n-1) + climb(n-2)
            return dict[n]
        return climb(n)


#Botom up 
#TC=O(n) because of memoization SC=O(1) 

class Solution:
    def climbStairs(self, n: int) -> int:
      ##recursion with memoization:
        one=1
        two=1
        for i in range(n-1):
            temp = one
            one = one+two
            two=temp
        return one