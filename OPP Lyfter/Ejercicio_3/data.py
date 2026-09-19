import csv
from menu import Student

def export_students_csv(student_list):
    if not student_list:
        print('No registered student found')
        return 
    with open("student_marks_list.csv", mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["name", "section", "spanish", "english", "social_studies", "science"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        # Convertimos cada objeto Student a diccionario con .to_dict()
        rows = [student.to_dict() for student in student_list]
        writer.writerows(rows)
        print('student_marks_list.csv was created')


def import_students_csv(filename="student_marks_list.csv"):
    imported_students_list = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Instanciamos el objeto Student con los datos leídos
                student = Student(
                    name=row["name"],
                    section=row["section"],
                    spanish=row["spanish"],
                    english=row["english"],
                    social_studies=row["social_studies"],
                    science=row["science"]
                )
                imported_students_list.append(student)
        return imported_students_list
    except FileNotFoundError:
        print('Error! The file was not found')
        return []