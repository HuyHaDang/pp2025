import curses

def listStudent(students_list):
   for s in students_list:
    print(s)


def listCourses(courses_list):
    print("\n--- List of Courses ---")
    if not courses_list:
        print("No courses yet.")
    for c in courses_list:
        # Accessing tuple indices: 0 is ID, 1 is Name
        print(c)

def showMark(students_list, courses_list, marks_dict):
   listCourses(courses_list)
   nameOfCourse=input("input the name of the course: ")
   print(f"mark for {nameOfCourse}")
   for student in students_list:
         key=(student.get_id(), nameOfCourse)
         print(f"Student: {student.get_name()}, Mark: {marks_dict[key]}")
      
def showGPA(students_list,courses_list,marks_dict):
   for student in students_list:
      student.calculateGPA(marks_dict, courses_list)
     
   students_list.sort(key=lambda x: x.get_gpa(), reverse=True)
   for student in students_list:
      print(student)

def draw_student_list(stdscr, students_list, courses_list, marks_dict):
  stdscr.clear()
  stdscr.border()
  stdscr.addstr(1,2, "MANAGEMENT SYSTEM")
  stdscr.addstr(2,2, f"{'ID':<10} | {'Name':<20} | {'GPA':<5}")
  row=3
  for student in students_list:
      student.calculateGPA(marks_dict, courses_list)
      

  students_list.sort(key =lambda x: x.get_gpa(), reverse=True)

  for student in students_list:
     stdscr.addstr(row,2,f"{student.get_id(): <10} | {student.get_name(): <20} | {student.get_gpa():<5}")
     row+=1
  stdscr.addstr(row + 2, 2, "Press any key to exit UI...")
      
      # 5. Wait for user input
  stdscr.refresh()               # Actually paint it to the screen
  stdscr.getch()