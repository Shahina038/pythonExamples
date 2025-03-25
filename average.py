n = int(input())  # Number of students
student_marks = {}  
    
for _ in range(n):
    line = input().split()
    name = line[0]
    marks = list(map(float, line[1:]))  # Convert marks to float
    student_marks[name] = marks
    
query_name = input()  # Name to query
    
if query_name in student_marks:
    avg_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg_marks:.2f}") 