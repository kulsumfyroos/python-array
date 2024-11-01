n = int(input("Enter the size: "))
arr = []
print("Enter elements:")
for i in range(n):
    element = int(input())
    arr.append(element)
new_array = sorted(arr)

print("Original array:", arr)
print("Sorted array:", new_array)
rank = []
for element in arr:
    rank_index = new_array.index(element)+1
    rank.append(rank_index)
print("Ranks:", rank)
