# num_students = int(input())
# students = {}

# for student in range(num_students):
#     student_name, grade = input().split()
#     if student_name in students.keys():
#         students[student_name].append(float(grade))
#     else:
#         students[student_name] = [float(grade)]

# for student, grades in students.items():
#     convert_grades_to_string = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
#     print(f"{student} -> {convert_grades_to_string} (avg: {sum(grades)/len(grades):.2f})")

print(list(map(lambda n: n * 2, [1, 2, 3, 4, 5])))