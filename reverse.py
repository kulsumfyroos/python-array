n=int(input("enter the size:"))
arr=[]
print("enter elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
print(arr)
p=0
q=len(arr)-1
while p<q:
    arr[p],arr[q]=arr[q],arr[p]
    p+=1
    q-=1
print(arr)