#1.	Write a Python Program to find sum of array?
def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return (sum)
arr = []
arr = [12, 3, 4, 15]
n = len(arr)
ans = _sum(arr)
print('Sum of the array is ', ans)

#2.	Write a Python Program to find largest element in an array?
arr=list(map(int,input("Enter the elements:").split()))
a=max(arr)
print(a)

#3.	Write a Python Program for array rotation?
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))

#4.	Write a Python Program to Split the array and add the first part to the end?
def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n - 1):
            arr[j] = arr[j + 1]

        arr[n - 1] = x
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
splitArr(arr, n, position)
for i in range(0, n):
    print(arr[i], end=' ')








