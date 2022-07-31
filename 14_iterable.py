user = {
    "Name": "Hamid",
    "age": 24,
    "city": "Sheikhupura"
}
for item in user.items():
    print(item)
for k, v in user.items():  # we can write just keys and value to print with out dictionary brackets
    print(k, v)
for item in user.keys():
    print(item)
for item in user.values():
    print(item)


#  we can iterate over list dictionary tuple set str except int