num_students = int(input())
students = {}

for student in range(num_students):
    student_name, grade = input().split()
    if student_name in students.keys():
        students[student_name].append(float(grade))
    else:
        students[student_name] = [float(grade)]

for student, grades in students.items():
# converts the list of floats to a list of strings and then joins them through the .join()
    convert_grades_to_string = ' '.join(map(lambda grade: f'{grade:.2f}', grades)) 
    print(f"{student} -> {convert_grades_to_string} (avg: {sum(grades)/len(grades):.2f})")

