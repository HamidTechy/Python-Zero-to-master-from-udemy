def highest_func(li):
    even = []
    for item in li:
        if item % 2 == 0:
            even.append(item)
    return max(even)


print(highest_func([12, 45, 56, 68, 34]))
