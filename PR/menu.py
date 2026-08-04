def display_menu():
    print("-------------------")
    print("     MAIN MENU     ")
    print("-------------------")
    print("Press the number of you choice")
    print("1. Add Student")
    print("2. View All Students")
    print("3. View Top 3 Students")
    print("4. View Class Average")
    print("5. Export to CSV")
    print("6. Import from CSV")
    print("7. Exit")
    

def get_student_info():

    name = input("Enter the student's name: ")
    section= input("Enter the student's section: ")
    spanish_grade = ask_number("spanish")
    english_grade = ask_number("english")
    social_studies_grade = ask_number("social_studies")
    science_grade = ask_number("science")
    print('retornado')
    return {
        "name": name,
        "section": section,
        "spanish": spanish_grade,
        "english": english_grade,
        "social_studies": social_studies_grade,
        "science": science_grade
    }
    


def ask_number(subject):
    while True:
        number= input(f'Enter the {subject} grade between 0 and 100: ')
        try:         
            subject_grade = int(number)
            if 0 <= subject_grade <=100:    
                return subject_grade
            print(f'Error! The {subject} grade must be between 0 and 100')
        except ValueError:
                print('Error! Please enter only whole numbers')


def ask_option():
    while True:
        number= input("Select an option (1-7): ")
        try:         
            option_number = int(number)
            if 1 <= option_number <=7:
                return option_number
            print(f'Error! Your option must be between 1 and 7.')
        except ValueError:
                print('Error! Please enter only whole numbers')





