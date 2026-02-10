#  school Management System
# Assignment 1




class Student:


    def _init_(self, name, roll, course, password):
        self.name = name
        self.roll = roll
        self.course = course
        self.__password = password     # private variable (Encapsulation)

    def get_password(self):
        return self.__password


# ----- Course Class 


class Course:
    def _init_(self, course_name):
        self.course_name = course_name


# -------- File Handling Functions 

def enroll_student(student):
    file = open("students.txt", "a")
    data = f"{student.name},{student.roll},{student.course},{student.get_password()}\n"
    file.write(data)
    file.close()
    print("Student enrolled successfully.\n")


def show_all_students():
    try:
        file = open("students.txt", "r")
        students = file.readlines()
        file.close()

        if not students:
            print("No students found.\n")
            return

        print("---- All Students ----")
        for s in students:
            name, roll, course, password = s.strip().split(",")
            print(f"Name: {name} | Roll: {roll} | Course: {course}")
        print()

    except FileNotFoundError:
        print("No student data file found.\n")


# ------ Main Program 

def main():
    while True:
        print("1. Enroll Student")
        print("2. Show All Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            roll = input("Enter roll number: ")
            course = input("Enter course name: ")
            password = input("Set password: ")

            course_obj = Course(course)
            student = Student(name, roll, course_obj.course_name, password)
            enroll_student(student)

        elif choice == "2":
            show_all_students()

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.\n")


