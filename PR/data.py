import csv

def export_students_csv(student_list):
    if not student_list:
            print('No registered student found')
            return 
    with open("student_marks_list.csv", mode='w' , newline='', encoding='utf-8') as file:
        fieldnames= ["name", "section", "spanish", "english", "social_studies", "science"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(student_list)
        print('student_marks_list.csv was created')

def import_students_csv(filename="student_marks_list.csv"):
    imported_students_list = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["spanish"] = int(row["spanish"])
                row["english"] = int(row["english"])
                row["social_studies"] = int(row["social_studies"])
                row["science"] = int(row["science"])

                imported_students_list.append(row)
        return imported_students_list
    except FileNotFoundError:
        print('Error! The file was not found')
        return []   
        
    