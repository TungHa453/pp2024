# Function to input the number of students
def input_number_of_students():
    while True:
        try:
            return int(input("Enter the number of students in the class: "))
        # Error check
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to input the number of courses
def input_number_of_courses():
    while True:
        try:
            return int(input("Enter the number of courses: "))
        # Error check
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to input student information
def input_student_information():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return {'id': student_id, 'name': student_name, 'dob': student_dob, 'marks': {}}

# Function to input course information
def input_course_information():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {'id': course_id, 'name': course_name}

# Function to input student marks for a course
def input_student_marks(students, courses):
    course_id = input("Enter course ID to input marks for (or 'b' to go back): ")
    if course_id == 'b':
        return

    course = next((c for c in courses if c['id'] == course_id), None)
    # Error check
    if not course:
        print("Invalid course ID. Please try again.")
        return

    while True:
        student_id = input("Enter student ID to input marks for (or 'b' to go back): ")
        if student_id == 'b':
            return

        student = next((s for s in students if s['id'] == student_id), None)
        if student:
            marks = input(
                f"Enter marks for student {student['name']} ({student['id']}) in course {course_id} (or 'b' to go back): ")
            if marks == 'b':
                return
            student['marks'][course_id] = marks
        # Error check
        else:
            print("Invalid student ID. Please try again.")

# Function to list all courses
def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"Course ID: {course['id']}, Course Name: {course['name']}")

# Function to list all students
def list_students(students):
    print("Students:")
    for student in students:
        print(f"Student ID: {student['id']}, Student Name: {student['name']}, Student DoB: {student['dob']}")

# Function to show student marks for a course
def show_student_marks(students, courses):
    print("Available courses:")
    for course in courses:
        print(f"Course ID: {course['id']}, Course Name: {course['name']}")

    while True:
        course_id = input("Enter course ID to show student marks (or 'b' to go back): ")
        if course_id == 'b':
            return

        course = next((c for c in courses if c['id'] == course_id), None)
        # Error check
        if not course:
            print("Invalid course ID. Please try again.")
        else:
            break

    print(f"Student marks for course {course_id}:")
    for student in students:
        if 'marks' in student and course_id in student['marks']:
            print(f"Student ID: {student['id']}, Student Name: {student['name']}, Marks: {student['marks'][course_id]}")

# Main function to run the program
def main():
    students = []
    courses = []
    num_students = 0
    num_courses = 0
    previous_course_id = None

    while True:
        print("\n\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Input number of students")
        print("2. Input student information")
        print("3. Input number of courses")
        print("4. Input course information")
        print("5. Input student marks")
        print("6. List courses")
        print("7. List students")
        print("8. Show student marks for a course")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            num_students = input_number_of_students()
            students = []
        elif choice == '2':
            if len(students) < num_students:
                input_student_information(students)
            # Wrong / nonlogical input check
            else:
                print("You have entered the maximum number of students.")
        elif choice == '3':
            num_courses = input_number_of_courses()
            courses = []
        elif choice == '4':
            if len(courses) < num_courses:
                input_course_information(courses)
            # Wrong / nonlogical input check
            else:
                print("You have entered the maximum number of courses.")
        elif choice == '5':
            if len(students) == num_students and len(courses) == num_courses:
                input_student_marks(students, courses)
            # Wrong / nonlogical input check
            else:
                print("Please input the correct number of students and courses first.")
        elif choice == '6':
            list_courses(courses)
        elif choice == '7':
            list_students(students)
        elif choice == '8':
            show_student_marks(students, courses)
        elif choice == '9':
            break
        # Wrong / nonlogical input check
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()