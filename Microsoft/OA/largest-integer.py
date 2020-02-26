def largestint(arr):
    map = set()
    largest = 0
    for num in arr:
        if -1 * num in map:
            pos = num if num > 0 else num * -1
            if pos > largest:
                largest = pos
        else:
            map.add(num)
    return largest