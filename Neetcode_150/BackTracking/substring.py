"""[abcde]=['a', 'ab', 'abc', 'abcd', 'abcde', 'b', 'bc', 'bcd', 'bcde', 'c', 'cd', 'cde', 'd', 'de', 'e']"""
class Solution:
    def countSubstrings(self, s: str) -> int:

        curr=[]
        final=[]
        def substring(s,i):
            if i>=len(s):
                return
            for j in range(i,len(s)):
                new_str=s[i:j+1]
                curr.append(new_str)
            substring(s,i+1)
        substring(s,0)
        print(curr)
        return 0    
