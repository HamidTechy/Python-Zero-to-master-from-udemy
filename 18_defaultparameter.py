# these are the default parmeter
def message(fname="Microinn", lname="Student"):
    print(f"Hello {fname} {lname} good morning have a nice day")

# positional argument 
message("Hamid", "Latif")
message()

# this is the keyword argument that increase readablitiy we give value with parametrer name
message(fname="Hamid", lname="Latif")
message("Hamid")