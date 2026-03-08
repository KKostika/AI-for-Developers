staff = {
    "Alice": 27,
    "Bob": 35,
    "Charlie": 22,
}

name = input("please enter a name: ")
age = staff.get(name, "not found")

print("Age:", age)
