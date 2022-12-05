
#This is easy question, trick is if we use string concatenation it gives Time limit exceeded error becasue they say + takes a lot of time 
#TC and SC O(s)
class Solution(object):
    def addSpaces(self, s, spaces):
        # new_word = ""
        # j=0
        # for i in spaces:
        #     new_word+=s[j:i]+" "
        #     j=i
        # if j<len(s):
        #     new_word+=s[j:]
        # return new_word
        new_word = []
        sp = set(spaces)
        for i,c in enumerate(s):
            if i in sp:
                new_word.append(" ")
            new_word.append(c)
        return "".join(new_word)

newobj = Solution()
print(newobj.addSpaces("HelloWorld",[2,4]))