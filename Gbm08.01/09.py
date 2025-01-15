### 🤔 Converts the first character to upper case
# txt = "hello, and welcome to my world."
# print(txt.capitalize())

### 🤔 The first character is converted to upper case, and the rest are converted to lower case:
# txt = "python is FUN!"
# print(txt.capitalize())

### 🤔 This method is similar to the lower() method, but the casefold() method is stronger
# txt = "Hello, And Welcome To My World!"
# print(txt.casefold())
# print(txt.lower())

### 🤔 string.center(length, character(optional))
# txt = "banana"
# print(txt.center(20))

# txt = "banana"
# print(txt.center(20,'o'))

### 🤔 string.count(value, start(optional), end(optional))
# txt = "I love apples, apple are my favorite fruit"
# print(txt.count('apple'))

# txt = "I love apples, apple are my favorite fruit"
# print(txt.count('apple', 10, 24))

### 🤔 Check if the string ends with a punctuation sign (.):
# txt = "Hello, welcome to my world"
# print(txt.endswith('d'))

# txt = "Hello, welcome to my world."
# print(txt.endswith('my world.'))

# txt = "Hello, welcome to my world."
# print(txt.endswith('my world.', 5, 11))

### 🤔 Check if the string ends with either the phrase "world." or "castle.":
# txt = "Hello, welcome to my castle"
# print(txt.endswith(('world','castle')))

### 🤔 The expandtabs() method sets the tab size to the specified number of whitespaces
# txt = "H\te\tl\tl\to"
# print(txt.expandtabs(1))

# txt = "Hello, welcome to my world."
# print(txt.find('e'))

# txt = "Hello, welcome to my world."
# print(txt.find('e', 5, 10))

# txt = "Hello, welcome to my world."
# print(txt.find("q")) ### 🤔 output: -1
# print(txt.index("q")) ### 🤔 output: ValueError

# # named indexes:
# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# # numbered indexes:
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# # empty placeholders:
# txt3 = "My name is {}, I'm {}".format("John",36)
# print(txt1)
# print(txt2)
# print(txt3)

### 🤔 The isalnum() method returns True if all the characters are alphanumeric,(a-z) and (0-9)
### Example of characters that are not alphanumeric: (space)!%&? etc
# txt = "Company12"
# print(txt.isalnum())

### 🤔 (a-z). not alphabet letters:(space)!%&?
# txt = "CompanyX"
# print(txt.isalpha())

# txt = "Company10"
# print(txt.isalpha())

### 🤔 (0-9)
# txt = "1234"
# print(txt.isdecimal())

# txt = "50800"
# print(txt.isdigit())

### 🤔 returns True if the string is a valid identifier, otherwise False
# txt = "Demo"
# print(txt.isidentifier())

# a = "MyFolder"
# b = "Demo002"
# c = "2bring"
# d = "my demo"
# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())

### Returns True if all characters in the string are lower case
# txt = "hello world!"
# print(txt.islower())

# a = "Hello world!"
# b = "hello 123"
# c = "mynameisPeter"
# print(a.islower())
# print(b.islower())
# print(c.islower())

### 🤔 Exponents, like ² and ¾ are also considered to be numeric values.
### 🤔 (0-9)
### 🤔 "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the (-) and the (.) are not
# txt = "565543"
# print(txt.isnumeric())
 
# c = "10km2"
# d = "-1"
# e = "1.5"
# print(a.isnumeric())
# print(b.isnumeric())
# print(c.isnumeric())
# print(d.isnumeric())
# print(e.isnumeric())

### 🤔 Returns True if all characters in the string are printable
# txt = "Hello! Are you #1?"
# x = txt.isprintable()
# print(x)

### 🤔 Check if all the characters in the text are whitespaces
# txt = "   "
# x = txt.isspace()
# print(x)

# txt = "   s   "
# x = txt.isspace()
# print(x)

### 🤔 all words in a text start with a upper case letter
# txt = "Hello, And Welcome To My World!"
# print(txt.istitle())

# a = "HELLO, AND WELCOME TO MY WORLD"
# b = "Hello"
# c = "22 Names"
# d = "This Is %'!?"
# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

# txt = "THIS IS NOW!"
# print(txt.isupper())

### 🤔 The join() method takes all items in an iterable and joins them into one string.
# myTuple = ("John", "Peter", "Vicky")
# x = ' + '.join(myTuple)
# print(x)

# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"
# x = mySeparator.join(myDict)
# print(x)


