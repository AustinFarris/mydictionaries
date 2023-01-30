person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# name of second child
print(person["children"][1])

# name of the cat
print(person["pets"]["cat"])

# loop to list each child
for child in person["children"]:
    print(child)


for i, j in person["pets"].items():
    print(f"Type of pet: {i} name of pet: {j}")
