import math
import numpy as np
import curses


class Student():
  def __init__(self, name, id, dob):
    self.__name=name
    self.__id=id
    self.__dob=dob
    self.__gpa = 0.0
    self.__marks= []
    self.__credits=[]

  def calculateGPA(self):
      self.__marks= []
      self.__credits=[]
      # for course in courses_list:         
      #    self.__credits.append(course.get_credits())
      for course in courses_list:
        key=(self.get_id(), course.get_name()) #get the key for dict
        if key in marks_dict:
           self.__credits.append(course.get_credits())
           self.__marks.append(marks_dict[key])
        else:
           continue   
      sumNumpy=np.sum(np.array(self.__marks)* np.array(self.__credits)) #sum of all the mark*credits
      self.__gpa=sumNumpy/np.sum(self.__credits)

      
  def __str__(self):
     return f"name: {self.__name}, id: {self.__id}, dob: {self.__dob}"
  def get_name(self):
     return self.__name
  def get_id(self):
     return self.__id
  def get_dob(self):
     return self.__dob
  def get_gpa(self):
     return self.__gpa
  def __str__(self):
     return f"ID: {self.__id}, name: {self.__name}, gpa: {self.__gpa}"

class Course():
   def __init__(self, name, id, credits):
      self.__name=name
      self.__id=id
      self.__credits=credits
   def __str__(self):
      return f"id: {self.__id}, name: {self.__name}"
   def get_name(self):
     return self.__name
   def get_id(self):
     return self.__id
   def get_credits(self):
     return self.__credits

# --- GLOBAL DATA STRUCTURES ---
# LIST of DICTIONARIES for studentxs
# Example: [{'id': 'BI12-001', 'name': 'Nam', 'dob': '01/01/2005'}]
students_list = []

# LIST of TUPLES for courses
# Example: [('CS01', 'Python'), ('CS02', 'Java')]
# We use tuples here because course info shouldn't change once created.
courses_list = []

# DICTIONARY with TUPLE KEYS for marks
# Example: {('BI12-001', 'CS01'): 15.5}
# Key is (student_id, course_id), Value is float mark
marks_dict = {}

def addStudent():
    numberOfStudent=int(input("number student: "))
    for i in range(numberOfStudent):
      id=input(f"Input id of student {i+1}: ")
      name=input(f"Input name of student: {i+1} ")
      dob=input(f"Input dob of student: {i+1} ")
      student=Student(name,id,dob)
      students_list.append(student)

def addCourse():
    numberOfCourse=int(input("number course: "))
    for i in range(numberOfCourse):
      id=input(f"Input id of course {i+1}: ")
      name=input(f"Input name of course {i+1}: ")
      credits=int(input(f"Input credits of course {i+1}: "))
      course=Course(name,id,credits)
      courses_list.append(course)

def listStudent():
   for s in students_list:
    print(s)
def listCourses():
    print("\n--- List of Courses ---")
    if not courses_list:
        print("No courses yet.")
    for c in courses_list:
        # Accessing tuple indices: 0 is ID, 1 is Name
        print(c)
        

def inputMark():
   if not courses_list:
        print("No courses available.")
        return
   listCourses()
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


def showMark():
   listCourses()
   nameOfCourse=input("input the name of the course: ")
   print(f"mark for {nameOfCourse}")
   for student in students_list:
         key=(student.get_id(), nameOfCourse)
         print(f"Student: {student.get_name()}, Mark: {marks_dict[key]}")
      
def showGPA():
   for student in students_list:
      student.calculateGPA()
     
   students_list.sort(key=lambda x: x.get_gpa(), reverse=True)
   for student in students_list:
      print(student)



      


def main():
  students_list.append(Student("huyhadang", 138, 1910)) 
  students_list.append(Student("abcxyz", 139, 2505)) 
  students_list.append(Student("xmn", 137, 2705)) 
  
  courses_list.append(  Course("python", "python", 4))
  courses_list.append(  Course("java", "java", 3))
  


  while True:
        print("\n==============================")
        print("STUDENT MARK MANAGEMENT (Tuples/Dicts/Lists)")
        print("1. Input students")
        print("2. Input courses")
        print("3. List students")
        print("4. List courses")
        print("5. Input marks for a course")
        print("6. Show marks for a course")
        print("7. Show GPA")
        print("0. Exit")
        
        choice = int(input("Your choice: ")) 
        match choice:
           case 1: addStudent()
           case 2: addCourse()
           case 3: listStudent()
           case 4: listCourses()
           case 5: inputMark()
           case 6: showMark()
           case 7: showGPA()
           case 0: break


main()