import heapq

def k_way_merge(arrays):
    k = len(arrays)
    min_heap = []

    # Initialization: Add the first element of each array to the heap
    for i in range(k):
        if arrays[i]:  # Ensure the array is not empty
            heapq.heappush(min_heap, (arrays[i][0], i, 0))

    output = []

    # Merge Process
    while min_heap:
        val, arr_idx, ele_idx = heapq.heappop(min_heap)
        output.append(val)

        # If there's another element in the same array, add it to the heap
        if ele_idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(min_heap, (arrays[arr_idx][ele_idx + 1], arr_idx, ele_idx + 1))

    return output

# Tester
arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

merged_array = k_way_merge(arrays)
print(merged_array)  # Output should be [1, 2, 3, 4, 5, 6, 7, 8, 9]