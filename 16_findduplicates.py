mylist = ["a", "b", "c", "d", "c", "e", "d"]
duplicates = []

for values in mylist:
    if mylist.count(values) > 1:
        if values not in duplicates:
            duplicates.append(values)
print(duplicates)