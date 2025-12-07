class Student():
  def __init__(self, name, id, dob):
    self.__name=name
    self.__id=id
    self.__dob=dob
  def __str__(self):
     return f"name: {self.__name}, id: {self.__id}, dob: {self.__dob}"
  def get_name(self):
     return self.__name
  def get_id(self):
     return self.__id
  def get_dob(self):
     return self.__dob
  

class Course():
   def __init__(self, name, id):
      self.__name=name
      self.__id=id
   def __str__(self):
      return f"id: {self.__id}, name: {self.__name}"
   def get_name(self):
     return self.__name
   def get_id(self):
     return self.__id

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
      course=Course(name,id)
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
    val = float(input(f"Enter mark for {student.get_name()} (ID: {student.get_id()}): "))
    key=(student.get_id(), nameOfCourse)
    marks_dict[key]=val
    print("successfully")


def showMark():
   listCourses()
   nameOfCourse=input("input the name of the course: ")
   print(f"mark for {nameOfCourse}")
   for student in students_list:
         key=(student.get_id(), nameOfCourse)
         print(f"Student: {student.get_name()}, Mark: {marks_dict[key]}")
      



def main():
  while True:
        print("\n==============================")
        print("STUDENT MARK MANAGEMENT (Tuples/Dicts/Lists)")
        print("1. Input students")
        print("2. Input courses")
        print("3. List students")
        print("4. List courses")
        print("5. Input marks for a course")
        print("6. Show marks for a course")
        print("0. Exit")
        
        choice = int(input("Your choice: ")) 
        match choice:
           case 1: addStudent()
           case 2: addCourse()
           case 3: listStudent()
           case 4: listCourses()
           case 5: inputMark()
           case 6: showMark()
           case 0: break


main()