from domains.course import Course
from domains.student import Student
from output import listCourses
import math
import zipfile
import os
import pickle 
import gzip

SAVE_FILE = "students.dat"

def save_data(students_list, courses_list, marks_dict):
   
   try:
      data=(students_list, courses_list, marks_dict)

      with gzip.open(SAVE_FILE, 'wb') as f:
         pickle.dump(data,f)
      print(f"Data successfully pickled and compressed to {SAVE_FILE}")

   except Exception as e:
      print(f"error saving data: {e}")


def load_data(students_list,courses_list, marks_dict):
   
   if os.path.exists(SAVE_FILE):
      with gzip.open(SAVE_FILE, 'rb') as f:
         loaded_data=pickle.load(f)
         loaded_students,loaded_course,loaded_marks=loaded_data
         students_list.clear()
         students_list.extend(loaded_students)
         courses_list.clear()
         courses_list.extend(loaded_course)
         marks_dict.clear()
         marks_dict.update(loaded_marks)
      print("Data loaded and restored successfully!")
      return True
   else: 
      print("no save file")
      return False
                           
 
               
               

            


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
       
   
   
   for student in students_list:
      val =float(input(f"Enter mark for {student.get_name()} (ID: {student.get_id()}): "))
      val1Digit=math.floor(val*10)/10
      
      key=(student.get_id(), nameOfCourse)
      marks_dict[key]=val1Digit
      print("successfully")
    
