# --- GLOBAL DATA STRUCTURES ---
# LIST of DICTIONARIES for students
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
      id=input("Input id of student: ")
      name=input("Input name of student: ")
      dob=input("Input dob of student: ")
      student={"id": id, "name": name, "dob":dob }
      students_list.append(student)

def addCourse():
    numberOfCourse=int(input("number course: "))
    for i in range(numberOfCourse):
      id=input("Input id of course: ")
      name=input("Input name of course: ")
      course={"id": id, "name": name}
      courses_list.append(course)

def listStudent():
   for s in students_list:
      print(f"ID: {s['id']}, name: {s["name"]}, dob: {s['dob']} ")

def listCourses():
    print("\n--- List of Courses ---")
    if not courses_list:
        print("No courses yet.")
    for c in courses_list:
        # Accessing tuple indices: 0 is ID, 1 is Name
        print(f"ID: {c["id"]}, Name: {c["name"]}")
        

def inputMark():
   if not courses_list:
        print("No courses available.")
        return
   listCourses()
   nameOfCourse=input("What is the course you wanna input marks: ")
   for course in courses_list:
      if course["name"]==nameOfCourse:
        break
      else:
         print("course not found")
   for student in students_list:
    val = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
    key=(student["id"], nameOfCourse)
    marks_dict[key]=val
    print("successfully")


def showMark():
   listCourses()
   nameOfCourse=input("input the name of the course: ")
   print(f"mark for {nameOfCourse}")
   for marks in marks_dict:
      for student in students_list:
         key=(student["id"], nameOfCourse)
         print(f"Student: {student['name']}, Mark: {marks_dict[key]}")

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
        
        choice = int(input("Your choice: ")) # Add int() here
        match choice:
           case 1: addStudent()
           case 2: addCourse()
           case 3: listStudent()
           case 4: listCourses()
           case 5: inputMark()
           case 6: showMark()
           case 0: break


main()