n=int(input("enter the size:"))
arr=[]
print("enter elements:")
for i in range(n):
    elements=int(input())
    arr.append(elements)
    arr.sort()
print(arr)
i=0
while i<n-1:
    if arr[i]==arr[i+1]:
        arr.pop(i+1)
        n-=1
    else:
        i+=1
        
print(arr)
print(len(arr))