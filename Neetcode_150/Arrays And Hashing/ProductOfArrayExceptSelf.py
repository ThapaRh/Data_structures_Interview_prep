"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""
#TC: O(N) SC: O(N)
#Creating two arrays left_product and right_product will contain the product of left and right
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod=[1]
        right_prod=[1]
        calcr=1
        calcl=1
        for i in range(1,len(nums)):
            calcl=calcl*nums[i-1]
            left_prod.append(calcl)
        for j in range(len(nums)-1,0,-1):
            calcr=calcr*nums[j]
            right_prod.append(calcr)
        product = []
        print(len(right_prod),len(left_prod))
        for i in range(len(nums)):
            product.append(left_prod[i]*right_prod[len(nums)-1-i])
        return product

#Modifying the same approach littlebit to get O(1) SC
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
