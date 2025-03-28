def linear_search(arr,target):
    size =len(arr)
    for i in range(0,size):
        if(arr[i]==target):
            return 1

    return -1

list= [5,1,0,5,5,3]
target=[0,2,2,2,2]

result = linear_search(list,target)

print(result)