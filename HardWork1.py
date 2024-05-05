grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

Midl_Student = {}

sorted_students = sorted(students)

for i, student in enumerate(sorted_students):
    Sum = sum(grades[i])
    count = len(grades[i])
    Midl_Students = Sum / count
    Midl_Student[student] = round(Midl_Students, 2)

print(Midl_Student)