def BinarySearch(arr, k):
    first = 0
    end = len(arr) - 1
    arr.sort()
    found = False

    while first <= end and not found:
        mid = (first + end) // 2

        if arr[mid] == k:
            found = True
            return found
        else:
            if k < arr[mid]:
                end = mid - 1
            else:
                first = mid + 1

    return found
