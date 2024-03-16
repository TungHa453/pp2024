import math
import numpy as np
import os
import zipfile
import pickle

class StudentRecord:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.scores = []
        self.credits = []

    def calculate_gpa(self):
        if not self.scores or not self.credits:
            return 0
        weighted_scores = np.array(self.scores) * np.array(self.credits)
        return np.sum(weighted_scores) / np.sum(self.credits)

class CourseData:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

class MarkData:
    def __init__(self, student, course, score):
        self.student = student
        self.course = course
        self.score = score

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_student_records(self):
        num_students = int(input("Enter the number of student records to input: "))
        for _ in range(num_students):
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            self.students.append(StudentRecord(id, name, dob))
        with open('student_records.pkl', 'wb') as f:
            pickle.dump(self.students, f)

    def input_course_data(self):
        num_courses = int(input("Enter the number of courses to input: "))
        for _ in range(num_courses):
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credit = int(input("Enter course credit: "))
            self.courses.append(CourseData(id, name, credit))
        with open('course_data.pkl', 'wb') as f:
            pickle.dump(self.courses, f)

    def input_marks_data(self):
        course_id = input("Select a course by ID: ")
        course = next((course for course in self.courses if course.id == course_id), None)
        if course is None:
            print("Course not found.")
            return
        for student in self.students:
            score = float(input(f"Enter score for student {student.name} in course {course_id}: "))
            score = math.floor(score * 10) / 10  # round down to 1 decimal place
            self.marks.append(MarkData(student, course, score))
            student.scores.append(score)
            student.credits.append(course.credit)
        with open('marks_data.pkl', 'wb') as f:
            pickle.dump(self.marks, f)

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(course.id, course.name)

    def list_student_records(self):
        print("Student Records:")
        for student in self.students:
            print(student.id, student.name, student.dob)

    def show_marks(self):
        course_id = input("Select a course by ID to show marks: ")
        for mark in self.marks:
            if mark.course.id == course_id:
                print(f"Mark for student {mark.student.name} in course {course_id}: {mark.score}")

    def show_gpa(self):
        student_id = input("Select a student by ID to show GPA: ")
        student = next((student for student in self.students if student.id == student_id), None)
        if student is None:
            print("Student not found.")
            return
        print(f"GPA for student {student.name}: {student.calculate_gpa()}")

def compress_data_files():
    with zipfile.ZipFile('student_data.zip', 'w') as zipf:
        for file in ['student_records.pkl', 'course_data.pkl', 'marks_data.pkl']:
            if os.path.exists(file):
                zipf.write(file)

def decompress_data_files():
    if os.path.exists('student_data.zip'):
        with zipfile.ZipFile('student_data.zip', 'r') as zipf:
            zipf.extractall()

def main():
    decompress_data_files()
    school_system = SchoolSystem()
    school_system.input_student_records()
    school_system.input_course_data()
    school_system.list_courses()
    school_system.list_student_records()
    num = int(input("Enter the number of courses that you have inputted: "))
    for _ in range(num):
        school_system.input_marks_data()
        school_system.show_marks()
        school_system.show_gpa()
    compress_data_files()

if __name__ == "__main__":
    main()