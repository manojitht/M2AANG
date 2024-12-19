dictionary = {
    "name": "Manojith",
    "age": 24,
    "course": "Computer Science"
}

name = dictionary["name"] # accessing the value with key
print(name)

dictionary["specialization"] = "Artificial Intelligence" # adding the key with value to the dictionary
print(dictionary)

if "age" in dictionary: # finding if key is in dictionary
    print(dictionary["age"])
else:
    print("age not there")

for key, value in dictionary.items():
    print(key, value) # dictionary.items() will be tuples and unpacked as key, value

del dictionary["age"] # deletes the key and value of age

print(dictionary)

print(dictionary.get("present", "absent")) # the get() is used to check the key, if it's not exists it will return as "absent"