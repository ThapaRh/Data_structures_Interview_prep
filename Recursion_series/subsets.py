# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
###################################################################################################################################################################
# The approach I took is recursion. Input output method where I will make recursive tree. Write code from recursive tree 
#The stupid error I ran into and spent hours fihguring out why my code didnot work is passing the variable directly. Python does passby reference and that caused my code to produce unexpected output.
#The solution to that problem was assigning old_value to new variable a=b[:]=>like this duh


def subsets(nums): #here nums array is passed and we gotta find subset of that
    arr = [] #since we need output in the form of 2d array 
    def recursive_subsets(nums,subset): #we pass two variable and do recursive solution.nums is input and subset is our output
        if len(nums)==0: #when our input is 0, thats when we get output
            arr.append(subset)
            return 
        new_nums = nums[:]
        new_subset = subset[:] #here we dont want the subset to take the reference by value of subset that we passed in first recursive function
        recursive_subsets(nums[1:],subset)
        new_subset.append(new_nums[0])
        recursive_subsets(new_nums[1:],new_subset)
        return
    recursive_subsets(nums,[])
    return arr
print(subsets([1,2,3]))

#how it's done in leetcode easy:
def subset_non_recur(nums):
    arr=[[]]
    for i in nums:
        arr+=[lst+[i] for lst in arr] #this short weird method I really don't recommend if you are trying to understand
    return arr
print(subset_non_recur([1,2,3]))


