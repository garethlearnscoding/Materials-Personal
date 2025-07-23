import csv

def extraction():
    book_path = "C:/Users/ryan_/Downloads/School/Resources/H2 Computing/Materials-Personal/Exercises/resources/BOOK.txt"
    loan_path = "C:/Users/ryan_/Downloads/School/Resources/H2 Computing/Materials-Personal/Exercises/resources/LOAN.txt"
    member_path = "C:/Users/ryan_/Downloads/School/Resources/H2 Computing/Materials-Personal/Exercises/resources/MEMBER.txt"

    with open(member_path, 'r') as member_file:
        reader = csv.reader(member_file)
        members = [row for row in reader]
        print(members)


extraction()