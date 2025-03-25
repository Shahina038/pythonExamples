# Get number of students
n = int(input())

# Create a nested list to store student data
students = []

# Read input data
for _ in range(n):
    name = input().strip()
    grade = float(input())
    students.append([name, grade])

# Sort the list based on grades
students.sort(key=lambda x: x[1])

# Find the second lowest grade
unique_grades = sorted(set(grade for _, grade in students))
second_lowest_grade = unique_grades[1]

# Get names of students with the second lowest grade
second_lowest_students = sorted([name for name, grade in students if grade == second_lowest_grade])

# Print names
for student in second_lowest_students:
    print(student)
