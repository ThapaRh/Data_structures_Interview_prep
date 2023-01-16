
def func(nums):
    i = 0
    count=0
    while(i+1<len(nums)):
        print(nums)
        print(i)
        if nums[i]==nums[i+1]:
            count+=1
            nums.pop(i)
            nums.pop(i)
            if i-1>=0:
                i=i-1
        else:
            i+=1
    if count%2 == 1:
        return "Alice"
    else:
        return "Bob"
    
print(func([1,5,5,1,1,1]))