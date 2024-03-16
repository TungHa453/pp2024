import math
import numpy as np
import os
import zipfile

class Learner:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.scores = []
        self.credits = []

    def calculate_cgpa(self):
        if not self.scores or not self.credits:
            return 0
        weighted_scores = np.array(self.scores) * np.array(self.credits)
        return np.sum(weighted_scores) / np.sum(self.credits)

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

class Mark:
    def __init__(self, learner, course, score):
        self.learner = learner
        self.course = course
        self.score = score

class University:
    def __init__(self):
        self.learners = []
        self.courses = []
        self.marks = []

    def input_learners(self):
        num_learners = int(input("Enter number of learners to input: "))
        for _ in range(num_learners):
            id = input("Enter learner id: ")
            name = input("Enter learner name: ")
            dob = input("Enter learner DoB: ")
            self.learners.append(Learner(id, name, dob))
        with open('learners.txt', 'w') as f:
            for learner in self.learners:
                f.write(f'{learner.id},{learner.name},{learner.dob}\n')

    def input_courses(self):
        num_courses = int(input("Enter number of courses to input: "))
        for _ in range(num_courses):
            id = input("Enter course id: ")
            name = input("Enter course name: ")
            credit = int(input("Enter course credit: "))
            self.courses.append(Course(id, name, credit))
        with open('courses.txt', 'w') as f:
            for course in self.courses:
                f.write(f'{course.id},{course.name},{course.credit}\n')

    def input_marks(self):
        course_id = input("Select a course by id: ")
        course = next((course for course in self.courses if course.id == course_id), None)
        if course is None:
            print("Course not found.")
            return
        for learner in self.learners:
            score = float(input(f"Enter score for learner {learner.name} in course {course_id}: "))
            score = math.floor(score * 10) / 10  # round down to 1 decimal place
            self.marks.append(Mark(learner, course, score))
            learner.scores.append(score)
            learner.credits.append(course.credit)
        with open('marks.txt', 'w') as f:
            for mark in self.marks:
                f.write(f'{mark.learner.id},{mark.course.id},{mark.score}\n')

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(course.id, course.name)

    def list_learners(self):
        print("Learners:")
        for learner in self.learners:
            print(learner.id, learner.name, learner.dob)

    def show_marks(self):
        course_id = input("Select a course by id to show marks: ")
        for mark in self.marks:
            if mark.course.id == course_id:
                print(f"Mark for learner {mark.learner.name} in course {course_id}: {mark.score}")

    def show_cgpa(self):
        learner_id = input("Select a learner by id to show CGPA: ")
        learner = next((learner for learner in self.learners if learner.id == learner_id), None)
        if learner is None:
            print("Learner not found.")
            return
        print(f"CGPA for learner {learner.name}: {learner.calculate_cgpa()}")

def compress_files():
    with zipfile.ZipFile('learners.dat', 'w') as zipf:
        for file in ['learners.txt', 'courses.txt', 'marks.txt']:
            if os.path.exists(file):
                zipf.write(file)

def decompress_files():
    if os.path.exists('learners.dat'):
        with zipfile.ZipFile('learners.dat', 'r') as zipf:
            zipf.extractall()

def main():
    decompress_files()
    university = University()
    university.input_learners()
    university.input_courses()
    university.list_courses()
    university.list_learners()
    num = int(input("Enter number of courses that you have inputted: "))
    for _ in range(num):
        university.input_marks()
        university.show_marks()
        university.show_cgpa()
    compress_files()

if __name__ == "__main__":
    main()