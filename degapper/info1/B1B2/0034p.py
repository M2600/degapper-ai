def quickSort(start, end):
    kijun = int((a[start] + a[end]) / 2)
    left = start
    right = end
    while True:
        while a[left] < kijun:
            left = left + 1
        while kijun < a[right]:
            right = right - 1
        if right <= left:
            break
        tmp = a[left]
        a[left] = a[right]
        a[right] = tmp
        left = left + 1
        right = right - 1
    if start < left - 1:
        quickSort(start, left - 1)
    if right + 1 < end:
        quickSort(right + 1, end)

a = [4, 8, 6, 5, 2, 1, 3, 9, 7]
print("整列前 =", a)
quickSort(0, len(a) - 1)
print("整列後 =", a)