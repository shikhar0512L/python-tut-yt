"""
Introduction to Loops
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

for loop
while loop
"""
name = 'Abhishek'
for i in name:
    print(i, end=", ")

# Example: iterating over a list:
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)

# Similarly, we can use loops for lists, sets and dictionaries.
"""
range():
What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

Here, we can use the range() function.

range(0,n-1) where n is the given number
"""
for k in range(5):
    # It will print from 0 to 4
    print(k)

# But we can also loop over a specific range.
for k in range(4,9): # range (y,y-1)
    print(k)

for k in range(4,9): # range (y,y-1)
    print(k)

"""
Step is used for increment or decrement in loops. 
For ex.   for k in range(1,12,3):
                  print(k)
It increases the value by three as 1,4,7,10
"""
for k in range(1,12,3):
    print(k)

