#similar to the one we did before but input output selection is quite tricky
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