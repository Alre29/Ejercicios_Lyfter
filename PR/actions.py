
def show_all_students(students_list):
    students = students_list
    print("\n--- REGISTERED STUDENTS ---")
    if len(students) == 0:
        print("No students registered yet.\n")
    else:
        for student in students:
            print(student)



def calculate_student_average(student):
    average_marks_students = (student["spanish"] + student["social_studies"] + student["english"] + student["science"])/4
    return average_marks_students


def show_top_3_students(students_list):
    if not students_list:
        print('No registered student found')
        return 
    students_list_ordered = sorted(students_list, key=calculate_student_average, reverse=True)
    top_3 = students_list_ordered[:3]

    print('\n---TOP 3 STUDENTS AVERAGE---\n')
    count = 1
    for student in top_3:

        average = calculate_student_average(student)
        print(f"{count} {student['name']} with an average of {round(average,2)}")
        count += 1

def show_total_average(students_list):
    if not students_list:
        print('No registered student found')
        return 
    total_sum = 0
    for student in students_list:
        total_sum += calculate_student_average(student)

    total_average= total_sum/len(students_list)
    print(f"The class average is {round(total_average,2)}") 

