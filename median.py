n=int(input("enter the size:"))
arr=[]
print("enter elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
print(arr)
n=len(arr)
arr.sort()
print(arr)
if n%2==1:
    median=arr[n//2]
else:
    n1=arr[n//2-1]
    n2=arr[n//2]
    median=(n1+n2)/2
print(median)
