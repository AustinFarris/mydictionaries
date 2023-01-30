import random

phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}
"""
mydictionary = dict(m=8, n=9)

print(mydictionary)


print(f"Number of key-value pairs: {len(phonebook)}")


print()
print("*****  start section 1 - print dictionary ********")
print()


print()
print("*****  end section 1 ********")
print()





print()
print("*****  start section 2 - search dictionary ********")
print()

#Case sensitive
name = "Chris"

if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} does not exist in the phonebook")

# Key error means there wasn't a match for your key


print()
print("*****  end section 2 ********")
print()





print()
print("*****  start section 3 - edit/append dictionary ********")
print()

print(phonebook)

# Chris already exists so it will attempt to add but won't make a copy just updates chris's phone number
phonebook["Chris"] = "555-4444"

#If key doesn't exist it will append to dictionary, new key value pair created and appended
phonebook["Joe"] = "555-0123"

print(phonebook)

print()
print("*****  end section 3 ********")
print()



print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

#If key doesn't exist this command will error out
print(phonebook)
del phonebook["Chris"]
print(phonebook)


print()
print("*****  end section 4 ********")
print()



print()
print("*****  start section 5 - iterate through keys, values, items ********")
print()

# default is the key
for key in phonebook:
    print(f"The key is : {key} and the value is {phonebook[key]}")

# .values() is a method that iterates through just the values
for value in phonebook.values():
    print(value)

for k, v in phonebook.items():
    print(f"The key is : {k} and the value is {v}")

#immutable
for ph_tuple in phonebook.items():
    print(ph_tuple)


print()
print("*****  end section 5 ********")
print()


print()
print("*****  start section 6 - using get and clear ********")
print()

# change upper and lower for different values
name = "chris"

phone = phonebook.get(name, "key not found")

print(phone)

#doesn't eliminate just clears all elements in object
phonebook.clear()

print(phonebook)

print()
print("*****  end section 6 ********")
print()


print()
print("*****  start section 7 - using pop method ********")
print()

# second is default option
remove = phonebook.pop("Chris", "not found")

print(remove)
print(phonebook)

print()
print("*****  end section 7 ********")
print()


print()
print("*****  start section 8 - using popitem ********")
print()

#last item popped out automatically
a = phonebook.popitem()

print(a)

print(phonebook)


print()
print("*****  end section 8 ********")
print()

"""
print()
print("*****  start section 9 - using random and converting to list ********")
print()

list_of_keys = list(phonebook)
random_key = random.choice(list_of_keys)

print(random_key)
print(phonebook[random_key])

# all in one line no variables, better
print(phonebook[random.choice(list(phonebook))])

print()
print("*****  end section 9 ********")
print()
