n=int(input("enter the size:"))
arr=[]
print("enter the elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
print(arr)
k=int(input("enter the search elenent:"))
if k in arr:
   print(f"element {k} found at index {arr.index(k)}")
else:
    print(f"element {k} not found")