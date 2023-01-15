"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4."""
class Solution:
    def rob(self, nums: List[int]) -> int:
        dict={}
        length=len(nums)
        def recur(i):
            if i>=length: #because I have to go all the way to 0th index bitch
                return 0
            if i in dict:
                return dict[i]
            val1 = recur(i+1)
            val2 = nums[i]+ recur(i+2)
            dict[i] = max(val1,val2)
            return dict[i]
        return recur(0)










        start = 0
        end = 0
        for i in range(len(nums)):
            temp = max(nums[i]+start,end)
            start=end 
            end = temp
        return end
