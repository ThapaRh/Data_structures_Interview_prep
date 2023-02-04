def candies(array):
    sum=len(array)
    i=0
    while(i<len(array)):
        if i-1>=0 and array[i]>array[i-1]:
            sum+=1
        if i+1<len(array) and array[i+1]<array[i]:
            sum+=1
        i+=1
    return sum

print(candies([2,0,3,4]))

