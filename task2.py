def get_letter_grade(average):
    if average >= 90:
        return 'S'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    elif average >= 40:
        return 'F'
    else:
        return 'U'

def get_gpa(letter_grade):
    gpa_scale = {
        'S': 10.0,
        'A': 9.0,
        'B': 8.0,
        'C': 7.0,
        'D': 6.0,
        'F': 5.0,
        'U': 0.0
    }
    return gpa_scale.get(letter_grade, 0.0)

def main():
    grades = {}

    while True:
        subject = input("Enter the subject or assignment (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break
        
        grade = float(input(f"Enter the grade for {subject}: "))
        grades[subject] = grade

    if not grades:
        print("No grades entered.")
        return
    
    total = sum(grades.values())
    count = len(grades)
    average = total / count

    letter_grade = get_letter_grade(average)
    gpa = get_gpa(letter_grade)

    print("\nGrades:")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")

    print(f"\nAverage Grade: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.2f}")

if __name__ == "__main__":
    main()

