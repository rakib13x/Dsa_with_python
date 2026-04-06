# allows for search O(1)
# Can't mutate keys, but can mutate values
# Hashing is a process of converting a given key into another value. A hash function is
# in python haspmap is called a dictionary.

# Creating a dictionary
student = {}  # empty dict
student["name"] = "Rafi"  # add key → value
student["age"] = 20
student["city"] = "Dhaka"

print(student["name"])  # → Rafi
print(student["age"])


# check if key exists
scores = {"Ali": 85, "Sara": 92}

# Safe way to check
if "Ali" in scores:
    print("Ali's score:", scores["Ali"])  # → 85

if "Karim" not in scores:
    print("Karim not found")  # → Karim not found

# .get() — returns None if key missing (no error)
print(scores.get("Nadia"))  # → None
print(scores.get("Nadia", 0))


# Counting items

fruits = ["apple", "banana", "apple", "mango", "banana", "apple"]

count = {}

for fruit in fruits:
    if fruit in count:
        count[fruit] += 1  # already seen, add 1
    else:
        count[fruit] = 1  # first time seeing it

print(count)


# --------------------------- basic problems ----------------------

# 1. Find the first repeated word

words = ["cat", "dog", "cat", "bird"]
seen = {}

for word in words:
    if word in seen:
        print(word)
        break  # stop immediately
    else:
        seen[word] = True

# 2. Find the most frequent item

items1 = ["cat", "dog", "cat", "bird", "cat"]


def most_frequent(items):
    newItem = {}
    for num in items:
        if num in newItem:
            newItem[num] += 1
        else:
            newItem[num] = 1

    best_item = None
    best_count = 0
    for item, number in newItem.items():
        if number > best_count:
            best_count = number
            best_item = item

    return best_item


# call the function and print the result
result = most_frequent(items1)
print(result)  # → cat
