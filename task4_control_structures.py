# Task 4: Control Structures - Selection & Looping
# File: task4_control_structures.py
# ---------------------------------------------------------
# a. if-elif-else: classify a student grade based on marks (5 marks)
# ---------------------------------------------------------
print("a. Grade Classification")
marks = 78  # sample input, change this value to test other grades
if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"
print("Marks:", marks)
print("Grade:", grade)
print()
# ---------------------------------------------------------
# b. for loop over a list of 5 fruits (3 marks)
# ---------------------------------------------------------
print("b. For Loop - Fruits")
fruits = ["Mango", "Banana", "Orange", "Pineapple", "Watermelon"]
for fruit in fruits:
    print(fruit)
print()
# ---------------------------------------------------------
# c. while loop: count 1 to 10, print only even numbers (3 marks)
# ---------------------------------------------------------
print("c. While Loop - Even Numbers 1 to 10")
count = 1
while count <= 10:
    if count % 2 == 0:
        print(count)
    count += 1
print()
# ---------------------------------------------------------
# d. break and continue with a practical example (varies, see marks)
# ---------------------------------------------------------
print("d. Break and Continue Example")
# Practical scenario: searching a list of registered student IDs.
# - 'continue' skips inactive/invalid IDs (represented as None).
# - 'break' stops the search as soon as the target ID is found.
student_ids = [101, 102, None, 104, 105, 106, None, 108]
target_id = 105
print("Searching for student ID:", target_id)
for student_id in student_ids:
    if student_id is None:
        # Skip missing/invalid records and move to the next one
        continue
    print("Checking ID:", student_id)
    if student_id == target_id:
        print("Student ID", target_id, "found! Stopping search.")
        break
