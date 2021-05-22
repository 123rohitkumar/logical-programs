def binary_search(arr,val):
    high = len(arr)
    low = 0

    while high>=low:

        mid = (high+low)//2

        if val == arr[mid]:
            return mid

        elif val<arr[mid]: 
            high = mid-1

        else:
            low = mid+1

arr = [4,6,7,9,12]
value = 9
res = binary_search(arr,value)
print(res)


