#similar to the one we did before but input output selection is quite tricky

# Given a string you need to print all possible strings that can be made by placing spaces (zero or one) in between them. The output should be printed in sorted increasing order of strings

# Example 1:

# Input:
# S = "ABC"
# Output: (A B C)(A BC)(AB C)(ABC)
# Explanation:
# ABC
# AB C
# A BC
# A B C
# These are the possible combination of "ABC".

#Tc and SC = O(n*2^n)
class Solution:
    def permutation (self, S):
        subset = ""
        subset+=S[0]
        arr = []
        def recur_permutation(word,subset):
            if len(word)==0:
                arr.append(subset)
                return
            op1=subset[:]+word[0]
            op2=subset[:]+" "+word[0]
            recur_permutation(word[1:],op1)
            recur_permutation(word[1:],op2)
        
        recur_permutation(S[1:],subset)
        return sorted(arr)
ob = Solution()
print(ob.permutation("apple"))