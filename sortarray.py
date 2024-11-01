n=int(input("enter the size:"))
arr=[]
print("enter elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
print(arr)
m=len(arr)
middle=m//2
first=sorted(arr[:middle])
second=sorted(arr[middle:],reverse=True)
print(first+second)
