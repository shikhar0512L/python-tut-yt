"""
Match Case Statements
To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python.

A match statement will compare a given variable's value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

The match case consists of three main entities :

The match keyword
One or more case clauses
Expression for each case
The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.

Syntax:
match variable_name:
            case 'pattern1' : //statement1
            case 'pattern2' : //statement2
            …            
            case 'pattern n' : //statement n
"""

# x = 4
x = int(input("Enter the value of x: "))

# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case _ if x % 2 == 0:
        print("x is  divisible by 2") 
    # Empty case with if-condition
    case _ if x<100:
        print("x is less than 100")
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)