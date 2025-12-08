from domains.course import Course
import curses
from domains.student import Student
from input import addCourse
from input import addStudent
from input import inputMark
from output import listCourses
from output import listStudent
from output import showMark
from output import draw_student_list
students_list = []

courses_list = []

marks_dict = {}

def main():
  students_list.append(Student("huyhadang", "138", 1910)) 
  students_list.append(Student("abcxyz", "139", 2505)) 
  students_list.append(Student("xmn", "137", 2705)) 
  
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
           case 1: addStudent(students_list)
           case 2: addCourse(courses_list)
           case 3: listStudent(students_list)
           case 4: listCourses(courses_list)
           case 5: inputMark(students_list, courses_list, marks_dict)
           case 6: showMark(students_list, courses_list, marks_dict)
          #  case 7: showGPA()
           case 7: 
              curses.wrapper(lambda stdscr: draw_student_list(stdscr, students_list, courses_list, marks_dict))
           case 0: break
            
main()