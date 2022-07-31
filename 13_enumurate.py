#  for i, char in enumerate("Helloo"):    # here we use enumerate to get the index i otherwise it will print just Hello
   #  print(i, char)

for i, char in enumerate(range(100)):
    print(i, char)
    if char == 50:
        print(f"the index number of 50 is {i}")
