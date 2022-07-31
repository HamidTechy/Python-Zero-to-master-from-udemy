# this is the parameter that we give in function start

def message(fname, lname):
    print(f"Hello {fname} {lname} good morning have a nice day")

# this is the arguments that we give when we call function


fname = input("enter your first name")
lname = input("enter your last name")
message(fname, lname)
