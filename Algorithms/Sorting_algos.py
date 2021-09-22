# merge sort

def merge_sort(list1):
    for i in range(len(list1)):
        key = list1[i]
        j = i-1
        while j>=0 and list1[j] > key:
            list1[j+1] = list1[j]
            j-=1
        list1[j+1] = key
    return list1


list1 = [0,2,1,4,2,7,3]
print(merge_sort(list1))
