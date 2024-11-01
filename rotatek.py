
n=int(input("enter the size:"))
arr=[]
print("enter elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
print(arr)
n=len(arr)
k=int(input("enter the k value:"))
first=arr[:-k]
second=arr[-k:]
print(second+first)