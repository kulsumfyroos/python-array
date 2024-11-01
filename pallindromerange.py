
min=int(input("enter the minimum range:"))
max=int(input("enter the maximum range:"))
d=0
for i in range(min,max+1,1):
    ori=i
    rev=0
    while i>0:
        d=i%10
        rev=rev*10+d
        i=i//10
    if rev==ori:
        print(rev)


    