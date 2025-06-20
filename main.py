def get_student_data(n, students=None):
    """Recursive function to gather student names and grades"""
    if students is None:
        students = []
    if n == 0:
        return students

    name = input(f"Enter name for student #{len(students)+1}: ")
    while True:
        try:
            grade = float(input(f"Enter grade for {name} (0-100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    students.append((name, grade))
    return get_student_data(n - 1, students)


def display_student_summary(students):
    print("\n--- Student Summary ---")
    for name, grade in students:
        print(f"{name}: {grade}")


def get_avg_grade(students):
    total = sum(grade for _, grade in students)
    return total / len(students)


def get_heighest_grade(students):
    return max(students, key=lambda x: x[1])


def count_passed(students):
    return sum(1 for _, grade in students if grade >= 60)


def main():
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students > 0:
                break
            else:
                print("Number must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    students = get_student_data(num_students)

    display_student_summary(students)

    avg = get_avg_grade(students)
    print(f"\nAverage grade of the class: {avg:.2f}")

    top_student = get_heighest_grade(students)
    print(f"Highest grade: {top_student[0]} with {top_student[1]}")

    passed_count = count_passed(students)
    print(f"Number of students who passed: {passed_count}")


if __name__ == "__main__":
    main()