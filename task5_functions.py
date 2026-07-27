# Task 5: Functions in Python
# File: task5_functions.py

# ---------------------------------------------------------
# a. Built-in functions: len(), max(), sorted() (3 marks)
# ---------------------------------------------------------
print("a. Built-in Functions")

scores = [67, 89, 45, 92, 78]

print("List of scores:", scores)
print("len(scores):", len(scores))
print("max(scores):", max(scores))
print("sorted(scores):", sorted(scores))
print()

# ---------------------------------------------------------
# b. User-defined function calculate_area(length, width) (4 marks)
# ---------------------------------------------------------
print("b. User-Defined Function - calculate_area")


def calculate_area(length, width):
    """Return the area of a rectangle given its length and width."""
    return length * width


area_result = calculate_area(10, 5)
print("Area of rectangle (length=10, width=5):", area_result)
print()

# ---------------------------------------------------------
# c. Function with default parameter values (4 marks)
# ---------------------------------------------------------
print("c. Function with Default Parameters")


def greet_student(name, course="Python Programming"):
    """Greet a student, using a default course if none is given."""
    print(f"Hello {name}, welcome to {course}!")


greet_student("Elizabeth", "Data Analysis")  # calling WITH the default overridden
greet_student("John")                        # calling WITHOUT specifying course (uses default)
print()

# ---------------------------------------------------------
# d. Function with *args - sum a variable number of arguments (3 marks)
# ---------------------------------------------------------
print("d. Function with *args")


def sum_numbers(*args):
    """Return the sum of any number of arguments passed in."""
    return sum(args)


print("sum_numbers(1, 2, 3):", sum_numbers(1, 2, 3))
print("sum_numbers(5, 10, 15, 20):", sum_numbers(5, 10, 15, 20))
print()

# ---------------------------------------------------------
# e. Lambda function to square a number, used with map() (3 marks)
# ---------------------------------------------------------
print("e. Lambda Function with map()")

square = lambda x: x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print()

# ---------------------------------------------------------
# f. Variable scope: local vs global, using the global keyword (3 marks)
# ---------------------------------------------------------
print("f. Variable Scope - Local vs Global")

school_name = "Cooperative University"  # global variable


def show_local_scope():
    """Demonstrate a local variable that only exists inside this function."""
    school_name = "Nairobi Institute"  # local variable, separate from the global one
    print("Inside function (local):", school_name)


def change_global_scope():
    """Demonstrate modifying the global variable using the 'global' keyword."""
    global school_name
    school_name = "Kenya Technical College"
    print("Inside function (after using global keyword):", school_name)


print("Before calling any function (global):", school_name)
show_local_scope()
print("After show_local_scope() call (global unchanged):", school_name)
change_global_scope()
print("After change_global_scope() call (global changed):", school_name)
