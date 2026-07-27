# Task 7: Scientific Modules - NumPy, Pandas & Matplotlib
# File: task7_numpy_pandas_matplotlib.py

# ---------------------------------------------------------
# a. Install NumPy, Pandas and Matplotlib using pip (3 marks)
# ---------------------------------------------------------
# These libraries are installed from the command line / terminal
# (NOT inside the Python script itself). Run the following command
# once, before running this script:
#
#     pip install numpy pandas matplotlib
#
# On some systems (e.g. Linux with an externally-managed Python), you
# may need:
#
#     pip install numpy pandas matplotlib --break-system-packages
#
# Once installed, they are imported below like any other module.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("a. Library Installation Check")
print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("Matplotlib version:", plt.matplotlib.__version__)
print()

# ---------------------------------------------------------
# b. NumPy: 1D array of 10 numbers, mean, sum, reshape to 2x5 (4 marks)
# ---------------------------------------------------------
print("b. NumPy - Array, Mean, Sum, Reshape")

numbers = np.array([12, 45, 67, 23, 89, 34, 56, 78, 90, 11])
print("Original 1D array:", numbers)

array_mean = numbers.mean()
array_sum = numbers.sum()
print("Mean of array:", array_mean)
print("Sum of array:", array_sum)

reshaped_array = numbers.reshape(2, 5)
print("Array reshaped to 2x5:")
print(reshaped_array)
print()

# ---------------------------------------------------------
# c. NumPy: two arrays, element-wise arithmetic (+, -, *, /) (4 marks)
# ---------------------------------------------------------
print("c. NumPy - Element-wise Arithmetic")

array_a = np.array([10, 20, 30, 40, 50])
array_b = np.array([1, 2, 3, 4, 5])

print("Array A:", array_a)
print("Array B:", array_b)
print("A + B:", array_a + array_b)
print("A - B:", array_a - array_b)
print("A * B:", array_a * array_b)
print("A / B:", array_a / array_b)
print()

# ---------------------------------------------------------
# d. Pandas: DataFrame from a dictionary - 4+ columns, 5 rows (5 marks)
# ---------------------------------------------------------
print("d. Pandas - Create DataFrame")

student_data = {
    "Name": ["Elizabeth", "John", "Mary", "Peter", "Grace"],
    "Age": [22, 24, 21, 23, 25],
    "Course": ["Python Programming", "Data Analysis", "Web Design",
               "Cybersecurity", "Networking"],
    "Marks": [78, 45, 89, 55, 40]
}

df = pd.DataFrame(student_data)
print(df)
print()

# ---------------------------------------------------------
# e. Pandas: filter rows where marks > 50 (4 marks)
# ---------------------------------------------------------
print("e. Pandas - Filter Marks > 50")

passed_students = df[df["Marks"] > 50]
print(passed_students)
print()

# ---------------------------------------------------------
# f. Matplotlib: bar chart of names vs marks (5 marks)
# g. Matplotlib: line graph showing a trend (5 marks)
# Both charts are drawn as subplots on ONE figure and saved
# together as a single .png file.
# ---------------------------------------------------------
print("f. Matplotlib - Bar Chart (Names vs Marks)")
print("g. Matplotlib - Line Graph (Trend)")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
average_marks_trend = [60, 63, 68, 72, 75, 80]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- f. Bar chart (left subplot) ---
ax1.bar(df["Name"], df["Marks"], color="skyblue")
ax1.set_title("Students' Marks")
ax1.set_xlabel("Student Name")
ax1.set_ylabel("Marks")

# --- g. Line graph (right subplot) ---
ax2.plot(months, average_marks_trend, marker="o", color="green")
ax2.set_title("Average Class Marks Trend Over 6 Months")
ax2.set_xlabel("Month")
ax2.set_ylabel("Average Marks")

plt.tight_layout()
plt.savefig("task7_charts.png")
plt.close()
print("Both charts saved together as task7_charts.png")
