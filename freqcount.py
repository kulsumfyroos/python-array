from collections import Counter

def sort_by_frequency(arr):
    # Step 1: Count the frequency of each element using Counter
    freq_map = Counter(arr)
    
    # Step 2: Sort the array by frequency (in descending order) and by element value (in ascending order)
    # Sorting by (-freq_map[x], x) ensures that:
    #   - First, elements are sorted by frequency in descending order
    #   - If two elements have the same frequency, they are sorted by their value in ascending order
    sorted_arr = sorted(arr, key=lambda x: (-freq_map[x], x))
    
    # Step 3: Print or return the sorted array
    return sorted_arr

# Example 1
arr1 = [1, 2, 3, 2, 4, 3, 1, 2]
result1 = sort_by_frequency(arr1)
print("Sorted array by frequency (Example 1):", result1)

# Example 2
arr2 = [-199, 6, 7, -199, 3, 5]
result2 = sort_by_frequency(arr2)
print("Sorted array by frequency (Example 2):", result2)
