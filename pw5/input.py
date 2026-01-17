from domains.course import Course
from domains.student import Student
from output import listCourses
import math
import zipfile
import os

def compress_data():
   files_to_compress=[]
   if os.path.exists("students.txt"):
      files_to_compress.append("students.txt")
   if os.path.exists("courses.txt"):
      files_to_compress.append("courses.txt")
   if os.path.exists("marks.txt"):
      files_to_compress.append("marks.txt")
   if not files_to_compress:
      print("not data to compress")
      return
   try:
      with zipfile.ZipFile('students.dat','w', zipfile.ZIP_DEFLATED) as zipf:
         for file in files_to_compress:
            zipf.write(file)
            print(f"Compress {file} into students.dat")
   except Exception as e:
      print(f"fail: {e}")


def decompress_data():
   if os.path.exists("students.dat"):
      try:
         with zipfile.ZipFile('students.dat', 'r') as zipf:
            zipf.extractall()
            print("data compressed successfully")
         return True
      except Exception as e:
         print(f"decompression failed: {e}")
   return False
   

def load_data(students_list,courses_list, marks_dict):
   if os.path.exists("students.txt"):
      with open("students.txt", "r") as f:
         while True:
            line=f.readline()
            # ID: 138 | NAME: hhd | DOB: 1910 
            if not line:
               break
            lineArray=line.strip().split("|")
            id=lineArray[0].split(":")[1].strip()
            name=lineArray[1].split(":")[1].strip()
            dob=lineArray[2].split(":")[1].strip()
            
            students_list.append(Student(name, id, dob))

   if os.path.exists("courses.txt"):
      with open("courses.txt", "r") as f:
         while True:
            line=f.readline()
            # ID: python | NAME: python | credits: 4 
            if not line:
               break
            lineArray=line.strip().split("|")
            id=lineArray[0].split(":")[1].strip()
            name=lineArray[1].split(":")[1].strip()
            credits=int(lineArray[2].split(":")[1])
            
            courses_list.append(Course(name, id, credits))


   if os.path.exists("marks.txt"):
      with open("marks.txt", "r") as f:
         for line in f:
            # COURSE python: tahuy: 13.0| hhd: 15.0| 
            line=line.strip()
            linePart=line.split(":", 1)
            nameCourse=linePart[0].replace("COURSE ","").strip()
            nameMarksArray=linePart[1].split("|")
            # A: 20
            for i in nameMarksArray:
               if i=="":
                  continue
               mark=i.strip().split(":") 
              #  A,20
               student_id = None
               for s in students_list:
                  if s.get_name() == mark[0].strip():
                      student_id = s.get_id()
                      break
              
               key=(student_id, nameCourse)
               marks_dict[key]=float(mark[1])
               
               

            


def addStudent(students_list):
    with open("students.txt", "a") as f:
      numberOfStudent=int(input("number student: "))
      for i in range(numberOfStudent):
        id=input(f"Input id of student {i+1}: ")
        name=input(f"Input name of student: {i+1} ")
        dob=input(f"Input dob of student: {i+1} ")
        
        f.write(f"ID: {id} | NAME: {name} | DOB: {dob} \n")

        student=Student(name,id,dob)
        students_list.append(student)

def addCourse(courses_list):
    with open("courses.txt", "a") as f:
      numberOfCourse=int(input("number course: "))
      for i in range(numberOfCourse):
        id=input(f"Input id of course {i+1}: ")
        name=input(f"Input name of course {i+1}: ")
        credits=int(input(f"Input credits of course {i+1}: "))
        f.write(f"ID: {id} | NAME: {name} | credits: {credits} \n")
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
       
   with open("marks.txt", "a") as f:
      f.write(f"COURSE {nameOfCourse}: ")
   with open("marks.txt", "a") as f:
    for student in students_list:
      val =float(input(f"Enter mark for {student.get_name()} (ID: {student.get_id()}): "))
      val1Digit=math.floor(val*10)/10
      f.write(f"{student.get_name()}: {val1Digit}| ")
      key=(student.get_id(), nameOfCourse)
      marks_dict[key]=val1Digit
      print("successfully")
    f.write("\n")
