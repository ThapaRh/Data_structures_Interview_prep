"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
#Tc= O(nlogn) Sc: O(1) if not used extra space and O(N) if used extra space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maximum=1
        count=1
        if nums==[]:
            return 0
        for i in range(1,len(nums)):
            if nums[i]-1==nums[i-1]:
                count+=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                maximum=max(count,maximum)
                count=1
        maximum=max(count,maximum)
        return maximum
    
#TC=O(N) SC=O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        maximum = 0
        for n in nums_set:
            if n-1 not in nums_set:
                new_num=n
                current_count=1

                while new_num + 1 in nums_set:
                    new_num+=1
                    current_count+=1
                maximum=max(maximum,current_count)
        return maximum
