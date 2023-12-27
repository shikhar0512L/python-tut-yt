"""
Python Tuples
Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

TUPLES ARE IMMUTABLE

"""
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(type(tuple1)) # <class 'tuple'>
print(tuple1)
print(tuple2)
details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)

"""
Tuple Indexes
Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on.

Example:
"""
country = ("Spain", "Italy", "India","Germany","USA","Canada","France","China")
#            [0]      [1]      [2]

"""
Accessing tuple items:
I. Positive Indexing:
As we have seen that tuple items have index, as such we can access items using these indexes.

Example:
"""
print(country[0])
print(country[1])
print(country[2])

"""
II. Negative Indexing:
Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

Example:
"""
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])

"""
Check for item:
We can check if a given item is present in the tuple. This is done using the in keyword.

Example 1:
"""
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

"""
IV. Range of Index:
You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.

Syntax:
Tuple[start : end : jumpIndex]

Note: jump Index is optional. We will see this in given examples.

Example: Printing elements within a particular range:
"""
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes

# Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values. Note: The element of the end index provided will not be included.

# Example: Printing all element from a given index till the end
print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes

# When no end index is provided, the interpreter prints all the values till the end.

#Example: printing all elements from start to a given index
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes

# When no start index is provided, the interpreter prints all the values from start up to the end index provided.

# Example: Print alternate values
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes

 #Here, we have not provided start and end index, which means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed.

print(animals[1:8:3])
# Here, jump index is 3. Hence it prints every 3rd element within given index.