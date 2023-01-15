"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if not nums:
            return 0
        length=len(nums)-1
        def recur(i,nums,dict):
            if i>=length:
                return 0
            if i in dict:
                return dict[i]
            val1 = nums[i] + recur(i+2,nums,dict)
            val2 = recur(i+1,nums,dict)
            dict[i]= max(val1,val2)
            return dict[i]
        val1 = recur(0,nums[:-1],{})
        val2 = recur(0,nums[1:],{})
        return max(val1,val2)


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]

        def check(num):
            if len(num)==1:
                return num[0]
            arr=[0 for i in range(len(num))]
            arr[0]=num[0]
            arr[1]=max(num[0],num[1])
            for i in range(2,len(num)):
                arr[i] = max(num[i]+arr[i-2],arr[i-1])
                print(i,arr[i])
            return arr[len(num)-1]

        val1=check(nums[1:])
        val2=check(nums[:-1])

        print(val1,val2)

        return(max(val1,val2))
