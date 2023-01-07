"""131. Palindrome Partitioning
Medium
9K
287
company
Bloomberg
company
Amazon
company
Adobe
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        curr=[]
        def DFS(i):
            if i>=len(s):
                res.append(curr[:])
                return
            for j in range(i,len(s)):
                if self.isPalin(s,i,j):
                    curr.append(s[i:j+1])
                    DFS(j+1)
                    curr.pop()
        DFS(0)
        return res
    def isPalin(self,s,i,j):
        while(i<=j):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        curr=[]
        new=[]
        def DFS(s,i,op):
            if i>=len(s):
                res.append(op)
                return
            val=op[:]
            if i<len(s) and len(op)!=0:
                op[-1]+=s[i]
            DFS(s, i+1 , op)
            val.append(s[i])
            DFS(s,i+1,val)
            return
                   
        DFS(s,1,[s[0]])
        
        if res:
            for v in res:
                flag=True
                for val in v:
                    if self.isPalin(val,0,len(val)-1)==False:
                        flag=False
                        break
                if flag:
                     new.append(v)  
        return new
    def isPalin(self,s,i,j):
        while(i<=j):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True