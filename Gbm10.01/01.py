### 🤔 Booleans
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)

### 🤔 With list comprehension you can do all that with only one line of code:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# newlist = [x for x in range(10)]
# print(newlist)

# newlist = [x for x in range(10) if x < 5]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x.upper() for x in fruits]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)

