def mergeSortedArrays(arr1, arr2):
    merged = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Append remaining elements from arr1 (if any)
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # Append remaining elements from arr2 (if any)
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

Recurrence Relation for Merge Sort:

T(n) = 2 * T(n/2) + O(n)
Here, T(n) represents the time it takes to sort an array of size n. The recurrence relation states that to sort an array of size n, we divide it into two halves of size n/2, recursively sort each half, and then merge the two sorted halves, which takes O(n) time.

The time complexity of merge sort in all three cases (best, worst, and average) is O(n log n)
