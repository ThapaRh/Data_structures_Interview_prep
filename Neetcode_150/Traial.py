class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(nums):
            dict[nums[i]]=[i] if nums[i] in dict else dict[nums[i]].append(i)
        print(dict)
    

item = Solution()
result = item.twoSum([2,7,11,15],9)
print(result)
