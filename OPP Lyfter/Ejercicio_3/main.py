from menu import display_menu, get_student_info, ask_option
from actions import show_all_students, show_top_3_students, show_total_average
from data import export_students_csv,import_students_csv

def main():

    students = []


    while True:

        display_menu()

        option = ask_option()

        match option:
            case 1:
                new_student = get_student_info()
                students.append(new_student)
                print("\n New student added!")
            case 2:
                show_all_students(students)
            case 3:
                show_top_3_students(students)
            case 4:
                show_total_average(students)          
            case 5:
                export_students_csv(students)
            case 6:
                loaded_data = import_students_csv()
                if loaded_data:
                    students = loaded_data
                    print("Data imported successfully!")
            case 7:
                print("Bye") 
                break

if __name__ == "__main__":
    main()