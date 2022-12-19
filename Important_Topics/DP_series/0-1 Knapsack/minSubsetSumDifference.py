#doesnot produce the correct answer yet
# understood concept but code doensot work for -ve numbers

class Solution(object):
    def minimumDifference(self, nums):
        total_sum = sum(nums) #summing total of the nums
        new_arr = [] # to store variables whose sum exists in subset_sum
        #we check if val in total_sum is subset sum of nums
        dictionary = {} # to memoize
        minimum = total_sum
        def subsetSum(sum,num,length):
            if length==len(num) and sum==0:
                return True
            if sum==0:
                return True
            if length==len(num):
                return False
            storage = num[length]
            if (sum,length) in dictionary:
                return dictionary[(sum,length)]
            if storage<=sum:
                dictionary[(sum,length)] = subsetSum(sum-storage,num,length+1) or subsetSum(sum,num,length+1)
                return dictionary[(sum,length)]
            else:
                dictionary[(sum,length)] = subsetSum(sum,num,length+1)
                return dictionary[(sum,length)]

        for i in range(total_sum):
            check = subsetSum(i,nums,0)
            if check:
                new_arr.append(i)
        
        val = (len(new_arr)//2)+1
        for j in range(0, val):
            if len(new_arr)==0:
                break    
            # print(j,'J')
            # print(new_arr,'array')
            # print(new_arr[j],"element")
            # print("/////////////////")
            minimum = min(minimum,abs(total_sum-(2*new_arr[j])))
            #print(minimum)
        
        return minimum
