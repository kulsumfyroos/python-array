def circular(arr, k):
   
   
    k = k % len(arr)

   
    rotate_array = arr[-k:] + arr[:-k]
    return rotate_array

arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
k = 2
result = circular(arr1, k)
print(result)
