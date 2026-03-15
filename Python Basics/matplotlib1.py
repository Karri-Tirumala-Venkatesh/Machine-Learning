import matplotlib.pyplot as plt

'''

# Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

plt.plot(x, y)
plt.show()

'''

# Bar Chart
students = ['Alice', 'Bob', 'Charlie']
grades = [85, 92, 78]

plt.title('Student Grades')
plt.xlabel('Student')
plt.ylabel('Grade')

plt.bar(students, grades)
plt.show()

# Scatter plot - used to show the correlation between two variables

height = [150, 160, 170, 175, 180, 185]
weight = [50, 60, 65, 70, 80, 85]

plt.scatter(height, weight)
plt.show()