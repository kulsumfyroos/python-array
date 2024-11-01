def custom_sort(arr1, arr2):
    order_map = {value: index for index, value in enumerate(arr2)}
    arr1.sort(key=lambda x: order_map.get(x, len(arr2) + x))
    return arr1
arr1 = [5, 3, 9, 1, 7, 3, 4]
arr2 = [3, 1, 4, 7] 
sorted_arr = custom_sort(arr1, arr2)
print("Sorted array:", sorted_arr)
  