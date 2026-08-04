from menu import display_menu, get_student_info, ask_option
from action import show_all_students, show_top_3_students, show_total_average
from data import export_students_csv,import_students_csv

def main():

    students = []
    test_students_list = [
    {
        "name": "Alice Smith",
        "section": "11A",
        "spanish": 95,
        "english": 88,
        "social_studies": 90,
        "science": 92
    },
    {
        "name": "Bob Johnson",
        "section": "11B",
        "spanish": 70,
        "english": 65,
        "social_studies": 80,
        "science": 75
    },
    {
        "name": "Charlie Brown",
        "section": "11A",
        "spanish": 100,
        "english": 98,
        "social_studies": 95,
        "science": 96
    },
    {
        "name": "Diana Prince",
        "section": "11B",
        "spanish": 85,
        "english": 80,
        "social_studies": 82,
        "science": 88
    }
]

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