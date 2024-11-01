n=int(input("enter the size:"))
arr=[]
print("enter elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
dict={}
for i in arr:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for key,values in dict.items():
    print({key},{values})

