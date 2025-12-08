from domains.course import Course
from domains.student import Student
from output import listCourses
import math

def addStudent(students_list):
    numberOfStudent=int(input("number student: "))
    for i in range(numberOfStudent):
      id=input(f"Input id of student {i+1}: ")
      name=input(f"Input name of student: {i+1} ")
      dob=input(f"Input dob of student: {i+1} ")
      student=Student(name,id,dob)
      students_list.append(student)

def addCourse(courses_list):
    numberOfCourse=int(input("number course: "))
    for i in range(numberOfCourse):
      id=input(f"Input id of course {i+1}: ")
      name=input(f"Input name of course {i+1}: ")
      credits=int(input(f"Input credits of course {i+1}: "))
      course=Course(name,id,credits)
      courses_list.append(course)

def inputMark(students_list,courses_list,marks_dict):
   if not courses_list:
        print("No courses available.")
        return
   listCourses(courses_list)
   nameOfCourse=input("What is the course you wanna input marks: ")
   for course in courses_list:
        if course.get_name() == nameOfCourse:
          break
        else:
         print("course not found")
   for student in students_list:
    val =float(input(f"Enter mark for {student.get_name()} (ID: {student.get_id()}): "))
    key=(student.get_id(), nameOfCourse)
    val1Digit=math.floor(val*10)/10
    marks_dict[key]=val1Digit
    print("successfully")
