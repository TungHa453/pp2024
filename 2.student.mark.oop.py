class Person:
    def __init__(self, person_id, person_name):
        self.person_id = person_id
        self.person_name = person_name


class Student(Person):
    def __init__(self, student_id, student_name):
        super().__init__(student_id, student_name)
        self.marks = {}

    def input_marks(self, course_id, marks):
        self.marks[course_id] = marks


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.num_students = 0
        self.num_courses = 0

    def input_number_of_students(self):
        while True:
            try:
                self.num_students = int(input("Enter the number of students in the class: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def input_number_of_courses(self):
        while True:
            try:
                self.num_courses = int(input("Enter the number of courses: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def input_person_information(self, person_type):
        person_id = input("Enter {} ID: ".format(person_type))
        person_name = input("Enter {} name: ".format(person_type))
        if person_type == "student":
            person = Student(person_id, person_name)
        else:
            person = Person(person_id, person_name)
        self.students.append(person) if person_type == "student" else None

    def input_course_information(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course = Course(course_id, course_name)
        self.courses.append(course)

    def input_student_marks(self):
        course_id = input("Enter course ID to input marks for (or 'b' to go back): ")
        if course_id == 'b':
            return

        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            print("Invalid course ID. Please try again.")
            return

        while True:
            student_id = input("Enter student ID to input marks for (or 'b' to go back): ")
            if student_id == 'b':
                return

            student = next((s for s in self.students if isinstance(s, Student) and s.person_id == student_id), None)
            if student:
                marks = input(
                    f"Enter marks for student {student.person_name} ({student.person_id}) in course {course_id} (or 'b' to go back): ")
                if marks == 'b':
                    return
                student.input_marks(course_id, marks)
            else:
                print("Invalid student ID. Please try again.")

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Course Name: {course.course_name}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            if isinstance(student, Student):
                print(f"Student ID: {student.person_id}, Student Name: {student.person_name}")

    def show_student_marks(self):
        print("Available courses:")
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Course Name: {course.course_name}")

        while True:
            course_id = input("Enter course ID to show student marks (or 'b' to go back): ")
            if course_id == 'b':
                return

            course = next((c for c in self.courses if c.course_id == course_id), None)
            if not course:
                print("Invalid course ID. Please try again.")
            else:
                break

        print(f"Student marks for course {course_id}:")
        for student in self.students:
            if isinstance(student, Student) and course_id in student.marks:
                print(f"Student ID: {student.person_id}, Student Name: {student.person_name}, Marks: {student.marks[course_id]}")

    def run(self):
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
                self.input_number_of_students()
                self.students = []
            elif choice == '2':
                if len(self.students) < self.num_students:
                    self.input_person_information("student")
                else:
                    print("You have entered the maximum number of students.")
            elif choice == '3':
                self.input_number_of_courses()
                self.courses = []
            elif choice == '4':
                if len(self.courses) < self.num_courses:
                    self.input_course_information()
                else:
                    print("You have entered the maximum number of courses.")
            elif choice == '5':
                if len(self.students) == self.num_students and len(self.courses) == self.num_courses:
                    self.input_student_marks()
                else:
                    print("Please input the correct number of students and courses first.")
            elif choice == '6':
                self.list_courses()
            elif choice == '7':
                self.list_students()
            elif choice == '8':
                self.show_student_marks()
            elif choice == '9':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = StudentManagementSystem()
    system.run()