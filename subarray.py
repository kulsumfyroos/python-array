n=int(input("enter the size:"))
arr=[]
print("enter the elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
print(arr)
m=int(input("enter the size:"))
arr1=[]
print("enter the elements:")
for i in range(m):
    elements=int(input())
    arr1.append(elements)
print(arr1)
for element in arr1:
    if element in arr:
        print("arr1 is subset")
    else:
        print("arr1 is not subset")  




"""
n = int(input("Enter the size of the first array: "))
arr = []
print("Enter the elements of the first array:")
for i in range(n):
    element = int(input())
    arr.append(element)

print("First array:", arr)

m = int(input("Enter the size of the second array: "))
arr1 = []
print("Enter the elements of the second array:")
for i in range(m):
    elements = int(input())
    arr1.append(elements)

print("Second array:", arr1)

# Check if arr1 is a subset of arr
is_subset = True  # Assume arr1 is a subset until proven otherwise

for element in arr1:
    if element not in arr:
        is_subset = False
        break  # No need to check further, arr1 is not a subset

if is_subset:
    print("arr1 is a subset of arr")
else:
    print("arr1 is not a subset of arr")
    """