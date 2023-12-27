# print("Hello world!")
# print("Hello I am a good boy \nand i love coding") # here \n is escape sequence character
# # This is a single line comment
# """
# This
# is
# a
# multiline
# comment
# """

# print("hey",6,7,sep="~")
# print("hey",6,7,sep="~",end="009\n")
# print("Shikhar")

# a=1
# b=True
# c="Shikhar"
# d=None
# e=0.577
# f=complex(5,3) # 5+3i
# # print(f)
# # # Printing the datatypes
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

# # List: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation
# list1 = [8, 2.3, [-4, 5], ["apple", "banana"] , ["Mango","ApplePie"]]
# print(list1)
# print(type(list1))

# # Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.
# tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
# print(tuple1)
# print(type(tuple1))

# # dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
# dict1 = {"name":"Ron", "age":15, "canVote":False}
# print(dict1)
# print(type(dict1))
 
# # Arithmetic operations

# print(5+6) # addition
# print(15-6) # Subtraction
# print(15*6) # Multiplicatiaon
# print(15/6) # Division : returns a float (if there)
# print(15//6) # floor division discards the fractional part
# print(5%3) # the % operator returns the remainder of the division
# print(2**4) # Exponential

# """
# Typecasting in python
# The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

# Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

# Two Types of Typecasting:
# Explicit Conversion (Explicit type casting in python)
# Implicit Conversion (Implicit type casting in python).
# Explicit typecasting:
# The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.

# It can be achieved with the help of Python's built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .

# Example of explicit typecasting:
# """
# string = "10"
# number = 7
# string_number = int(string) #throws an error if the string is not a valid integer
# sum= number + string_number
# print("The Sum of both the numbers is: ", sum)

# """
# Implicit type casting:
# Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.

# Python converts a smaller data type to a higher data type to prevent data loss.

# Example of implicit type casting:
# """
# # # Python automatically converts
# # # a to int
# g = 7
# print(type(g))
 
# # # Python automatically converts b to float
# h = 3.0
# print(type(h))
 
# # # Python automatically converts c to float as it is a float addition
# i = g + h
# print(i)
# print(type(i))

# # In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable
# j = input("Enter your name: ")
# print("My name is", j)

# k = input("Enter first number: ")
# l = input("Enter second number: ")
# # It will take the default value as a string

# print(k  + l) # Type : string
# print(int(k) + int(l)) # type : integer

# # #In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.
# name = "Shikhar"

# print("Hello, " + name)
# print('He said, "I want to eat an apple".')
# m = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""

# print(m)

# #In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
# # Square brackets can be used to access elements of the string.

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])
# # print(name[7]) # WILL THROW AN ERROR because 7th index dosen't exists.

# # #We can loop through strings using a for loop like this:
# for character in name:
#     print(character)
# #Above code prints all the characters in the string name one by one!

# # #We can find the length of a string using len() function.
# fruit = "Shikhar is a good boy"
# len1 = len(fruit)
# print(len1)
# # print("Mango is a", len1, "letter word.")

# # A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.
# pie = "ApplePie"
# print(pie[:5]) # [0,n-1] {Includes 0 but not 5}
# print(pie[6])	#returns character at specified index


# pieX = "BananaPie"
# print(pieX[:5])      #Slicing from Start
# print(pieX[5:])      #Slicing till End
# print(pieX[2:6])     #Slicing in between
# print(pieX[-8:])     #Slicing using negative index

# # DEFAULT print(var[0:len(var)])

# # # Strings are arrays and arrays are iterable. Thus we can loop through strings.
# alphabets = "codeWithShikhar"
# for i in alphabets:
#     print(i)
















""" 
String methods
Python provides a set of built-in methods that we can use to alter and modify the strings.

upper() :
The upper() method converts a string to upper case.

"""
str1 = "AbcDEfghIJ"
print(str1.upper())

# # lower() : The lower() method converts a string to lower case.
str2 = "AbcDEfghIJ8967"
print(str2.lower())

# # strip() : The strip() method removes any white spaces before and after the string.
str3 = " Silver Spoon "
print(str3.strip())

# #rstrip() : the rstrip() removes any trailing characters. Example:
str4 = "Hello !!!"
print(str4.rstrip("!"))

# #replace() : The replace() method replaces all occurences of a string with another string. Example:
str5 = "Silver Spoon"
print(str5.replace("Sp", "M"))

# #split() : The split() method splits the given string at the specified instance and returns the separated strings as list items.
str6 = "Silver Spoon"
print(str6.split(" "))      #Splits the string at the whitespace " ".

# # capitalize() : The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
str7 = "hello"
capStr7 = str7.capitalize()
print(capStr7)
str8 = "hello WorlD"
capStr8 = str8.capitalize()
print(capStr8)

# # center() : The center() method aligns the string to the center as per the parameters given by the user.
str9 = "Welcome to the Console!!!"
print(str9.center(50))
# # We can also provide padding character. It will fill the rest of the fill characters provided by the user.

str10 = "Welcome to the Console!!!"
print(str10.center(50, "."))

# # count() : The count() method returns the number of times the given value has occurred within the given string.
str12 = "Abracadabra"
countStr = str12.count("a")
print(countStr)

# # endswith() : The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str13 = "Welcome to the Console !!!"
print(str13.endswith("!!!"))

# #We can even also check for a value in-between the string by providing start and end index positions.
str14 = "Welcome to the Console !!!"
print(str14.endswith("to", 4, 10))

# # find() : The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
str15 = "He's name is Dan. He is an honest man."
print(str15.find("is"))

# # As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.
str16 = "He's name is Dan. He is an honest man."
print(str16.find("Daniel"))

# # index() : The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
str17 = "He's name is Dan. Dan is an honest man."
print(str17.index("Dan"))

# # As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.
str18 = "He's name is Dan. Dan is an honest man."
# print(str18.index("Daniel")) # {THROWS AN ERROR}

# # isalnum() : The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
# str19 = "WelcomeToTheConsole"
# print(str19.isalnum())

# # isalpha() : The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
st = "Welcome"
print(st.isalpha())

# # islower() : The islower() method returns True if all the characters in the string are lower case, else it returns False.
n = "hello world"
print(n.islower())

# # isprintable() : The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
o = "We wish you a Merry Christmas"
print(o.isprintable())

# # isspace() : The isspace() method returns True only and only if the string contains white spaces, else returns False.
p = "        "       #using Spacebar
print(p.isspace())
q = "        "       #using Tab
print(q.isspace())

# # istitle() : The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
r = "World Health Organization" 
print(r.istitle())

# # isupper() : The isupper() method returns True if all the characters in the string are upper case, else it returns False.
s = "WORLD HEALTH ORGANIZATION" 
print(s.isupper())

# # startswith() : The endswith() method checks if the string starts with a given value. If yes then return True, else return False.
t = "Python is a Interpreted Language" 
print(t.startswith("Python"))

# # swapcase() : The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
u = "Python is a Interpreted Language"
print(u.swapcase())

# # title() : The title() method capitalizes each letter of the word within the string.
v = "He's name is Dan. Dan is an honest man."
print(v.title())

# # Interview based HINT : Strings are immutable => the strings operators creates a new string resulting the operations. NOTE -> original value of the string can't be changed.