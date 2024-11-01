n=int(input("enter the size:"))
arr=[]
print("enter elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
print(arr)
sum=0
for i in range(n):
    sum=sum+arr[i]
    
print(sum)