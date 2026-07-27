
age = 22
print("a. Integer Variable")
print("Age:", age)
print("Type of age:", type(age))
print()


course_fee = 25000.50
fee_with_discount = course_fee - 2500.75
print("b. Float Variable")
print("Course Fee:", course_fee)
print("Type of course_fee:", type(course_fee))
print("Fee after discount (course_fee - 2500.75):", fee_with_discount)
print()
  
is_enrolled = True
print("c. Boolean Variable")
print("Is Enrolled:", is_enrolled)
if is_enrolled:
    print("Status: The student is currently enrolled.")
else:
    print("Status: The student is not enrolled.")
print()


first_name = "Elizabeth"
last_name = "Mwangi"
full_name = first_name + " " + last_name  
print("d. String Variable")
print("Full Name (concatenation):", full_name)
print("First 4 letters (slicing):", full_name[0:4])
print("Last 3 letters (slicing):", full_name[-3:])
print("Length of full name (len()):", len(full_name))
print()


subjects = ["Python", "Databases", "Networking", "Web Design", "Statistics"]
print("e. List")
print("Original list:", subjects)

subjects.append("Cybersecurity")
print("After append('Cybersecurity'):", subjects)

subjects.remove("Networking")
print("After remove('Networking'):", subjects)

print("Element at index 0:", subjects[0])
print("Element at index 2:", subjects[2])
print()


coordinates = (10, 20, 30)
print("f. Tuple")
print("Tuple:", coordinates)
try:
    coordinates[0] = 99 
except TypeError as e:
    print("Error caught while trying to modify tuple:", e)
print()

numbers = {1, 2, 2, 3, 4, 4, 4, 5}
print("g. Set")
print("Set (duplicates automatically removed):", numbers)
print()


student = {
    "name": "Elizabeth",
    "course": "Python Programming",
    "age": 22
}
print("h. Dictionary")
print("Original dictionary:", student)


print("Accessing 'name':", student["name"])


student["school"] = "Cooperative University"
print("After adding 'school' key:", student)

#del student["age"]
print("After deleting 'age' key:", student)
print()

num_str = "15"
num_int = int(num_str)      
num_float = float(num_int)  
back_to_str = str(num_float)  

print("i. Type Casting")
print("Original string:", num_str, "| Type:", type(num_str))
print("Converted to int:", num_int, "| Type:", type(num_int))
print("Converted to float:", num_float, "| Type:", type(num_float))
print("Converted back to string:", back_to_str, "| Type:", type(back_to_str))
