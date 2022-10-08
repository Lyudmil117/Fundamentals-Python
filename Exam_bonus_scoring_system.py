number_students = int(input())
total_number_lectures = int(input())
additional_bonus = int(input())
total_bonus = 0
max_bonus = 0
max_num_attendances = 0

for student in range(number_students):
    student_attendances = int(input())
    total_bonus = student_attendances / total_number_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
    if student_attendances > max_num_attendances:
        max_num_attendances = student_attendances

    max_bonus = round(max_bonus)

print(f'Max Bonus: {max_bonus}.')
print(f"The student has attended {max_num_attendances} lectures.")