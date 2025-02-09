def is_max_heap(arr):
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):
        if arr[i] < arr[2 * i + 1] or (2 * i + 2 < n and arr[i] < arr[2 * i + 2]):
            return False
    return True

# ตัวอย่างการใช้งาน
arr1 = [8, 5, 7, 1, 2, 6, 3, 4]
arr2 = [5, 4, 3, 1, 2]
arr3 = [1, 2, 3, 4, 5]

print(f"{arr1} เป็น Max Heap: {is_max_heap(arr1)}")
print(f"{arr2} เป็น Max Heap: {is_max_heap(arr2)}")
print(f"{arr3} เป็น Max Heap: {is_max_heap(arr3)}")