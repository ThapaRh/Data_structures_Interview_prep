#https://leetcode.com/problems/next-greater-element-i/submissions/1024288226/

from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash_map = defaultdict(int)
        final = [-1]*len(nums1)
        for i in range(len(nums1)):
            hash_map[nums1[i]]=i
        for j in range(len(nums2)):
            while len(stack)>0 and nums2[j]>stack[-1]:
                val = stack.pop()
                final[hash_map[val]]=nums2[j]
            if nums2[j] in hash_map:
                stack.append(nums2[j])
            
        return final