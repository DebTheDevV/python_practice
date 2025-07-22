marks = {"harry": 34, "jack": 45, "lily": 94}

# Making copies to experiment on
a = marks.copy()
b = marks.copy()
c = marks.copy()
d = marks.copy()
e = marks.copy()
f = marks.copy()
g = marks.copy()

# Accessing keys and values
print("Keys:", marks.keys())
print()
print("Values:", marks.values())
print()

# Removing a specific key
marks.pop("lily")
print("After pop('lily'):", marks)
print()

# Clearing the dictionary
marks.clear()
print("After clear():", marks)  # returns {}
print()

# ✅ Using dictionary methods correctly

# a.fromkeys() needs at least 1 argument — use it as a **class method**, not on an instance
new_dict = dict.fromkeys(["a", "b", "c"], 0)
print("fromkeys:", new_dict)
print()

# b.get() needs a key to fetch
print("get:", b.get("jack"))  # Returns 45
print()

# c.items() returns (key, value) pairs
print("items:", c.items())
print()

# d.popitem() removes the last inserted pair
print("popitem:", d.popitem())
print()
print("After popitem:", d)
print()

# The .setdefault() method in Python is used to:
# 	1.	Get the value of a key if it exists, or
# 	2.	Insert the key with a default value if it doesn’t exist

# e.setdefault()can be used like this:
print("setdefault:", e.setdefault("sam", 99))  # Adds 'sam' if not present
print()
print("After setdefault:", e)
print()

# f.update() takes a dictionary as input
f.update({"new": 100, "harry": 77})
print("After update:", f)
print()
