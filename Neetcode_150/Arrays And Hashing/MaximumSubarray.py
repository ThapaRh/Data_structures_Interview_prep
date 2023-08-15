#TC: O(n) SC = O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = -math.inf
        old = 0
        for new in nums:
            if old+new<=new:
                old = new
            else:
                old = old+new
            maximum = max(maximum,old)
        return maximum
                
                




        
        
        