
#this is how we create dictionary in python
list_1= [1,2,3,1,2,3,2,4,5]
dict = {}
for num in list_1:
    if num in dict:
        dict[num]+=1
    else:
        dict[num] = 1
print(dict)