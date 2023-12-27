"""
List Methods

list.sort()

This method sorts the list in ascending order. The original list is updated
"""
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

# What if you want to print the list in descending order?
# We must give reverse=True as a parameter in the sort method.

colors.sort(reverse=True)
print(colors)

num.sort(reverse=True)
print(num)

# The reverse parameter is set to False by default.
# Note: Do not mistake the reverse parameter with the reverse method.

"""
reverse()
This method reverses the order of the list.
"""
colors.reverse()
print(colors)

num.reverse()
print(num)

"""
index()
This method returns the index of the first occurrence of the list item.
"""
print(colors.index("green"))
print(num.index(3))

"""
count()
Returns the count of the number of items with the given value.
"""
print(num.count(2))

"""
copy()
Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
"""
newlist = colors.copy()
print(colors)
print(newlist)

"""
append():
This method appends/adds items to the end of the existing list.
"""
colors.append("orange")
print(colors)

"""
insert():
This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
"""

colors.insert(1, "red")
print(colors)

"""extend():
This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
"""
newColor = ["cyan", "brown", "aqua", "gold"]
colors.extend(newColor)
print(colors)

"""
Concatenating two lists:
You can simply concatenate two lists to join two lists.
"""
num2 = [12,45,67,654,32,56]
print(num+num2)