"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

# TC: O(N logk) SC: O(N+k)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        array = []
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        new_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        i=0
        for m,n in new_dict:
            if i>=k:
                break
            else:
                array.append(m)
                i+=1
        return array
        

