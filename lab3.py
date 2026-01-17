import math
import numpy as np
import curses
from curses import wrapper

class Student:
    def __init__(self, s_id, name, dob):
        self.id = s_id
        self.name = name
        self.dob = dob
        self.marks = {}  # Dictionary to map course_id -> mark
        self.gpa = 0.0

    def add_mark(self, course_id, mark):
        # Requirement: Use math module floor() to round-down to 1-digit decimal
        # Logic: 8.79 -> 87.9 -> floor(87) -> 87 -> 8.7
        rounded_mark = math.floor(mark * 10) / 10
        self.marks[course_id] = rounded_mark

    def calculate_gpa(self, courses):
        """
        Calculate GPA using Numpy arrays.
        Weighted sum = sum(mark * credit) / sum(credits)
        """
        if not self.marks:
            self.gpa = 0.0
            return

        credit_array = []
        mark_array = []

        for course in courses:
            if course.id in self.marks:
                credit_array.append(course.credits)
                mark_array.append(self.marks[course.id])
        
        if not credit_array:
            self.gpa = 0.0
            return

        # Requirement: Use numpy module and its array
        np_credits = np.array(credit_array)
        np_marks = np.array(mark_array)

        # Requirement: Weighted sum
        total_weighted_score = np.sum(np_marks * np_credits)
        total_credits = np.sum(np_credits)

        if total_credits == 0:
            self.gpa = 0.0
        else:
            self.gpa = total_weighted_score / total_credits

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | GPA: {self.gpa:.2f}"

class Course:
    def __init__(self, c_id, name, credits):
        self.id = c_id
        self.name = name
        self.credits = credits

class SchoolManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def sort_students_by_gpa(self):
        # Requirement: Sort student list by GPA descending
        # We ensure GPAs are updated before sorting
        for s in self.students:
            s.calculate_gpa(self.courses)
        
        # Sort descending
        self.students.sort(key=lambda x: x.gpa, reverse=True)

# --- Curses UI Helper Functions ---

def get_input(stdscr, r, c, prompt):
    """Helper to get string input in Curses"""
    stdscr.addstr(r, c, prompt)
    curses.echo() 
    input_bytes = stdscr.getstr(r, c + len(prompt))
    curses.noecho()
    return input_bytes.decode('utf-8')

def draw_menu(stdscr, selected_row_idx, menu_items):
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    
    title = "STUDENT MANAGEMENT SYSTEM (CURSES UI)"
    stdscr.addstr(0, w//2 - len(title)//2, title, curses.A_BOLD)

    for idx, row in enumerate(menu_items):
        x = w//2 - len(row)//2
        y = h//2 - len(menu_items)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    
    stdscr.refresh()

def add_student_ui(stdscr, system):
    stdscr.clear()
    stdscr.addstr(0, 0, "--- ADD NEW STUDENT ---", curses.A_BOLD)
    
    try:
        s_id = get_input(stdscr, 2, 0, "Enter ID: ")
        name = get_input(stdscr, 3, 0, "Enter Name: ")
        dob = get_input(stdscr, 4, 0, "Enter DoB: ")
        
        system.add_student(Student(s_id, name, dob))
        stdscr.addstr(6, 0, "Student added! Press any key...")
    except Exception:
        stdscr.addstr(6, 0, "Error input. Press any key...")
    
    stdscr.getch()

def add_course_ui(stdscr, system):
    stdscr.clear()
    stdscr.addstr(0, 0, "--- ADD NEW COURSE ---", curses.A_BOLD)
    
    try:
        c_id = get_input(stdscr, 2, 0, "Enter Course ID: ")
        name = get_input(stdscr, 3, 0, "Enter Course Name: ")
        credits_str = get_input(stdscr, 4, 0, "Enter Credits: ")
        
        system.add_course(Course(c_id, name, int(credits_str)))
        stdscr.addstr(6, 0, "Course added! Press any key...")
    except ValueError:
        stdscr.addstr(6, 0, "Invalid credit number. Press any key...")
    
    stdscr.getch()

def input_marks_ui(stdscr, system):
    stdscr.clear()
    stdscr.addstr(0, 0, "--- INPUT MARKS ---", curses.A_BOLD)
    
    if not system.students or not system.courses:
        stdscr.addstr(2, 0, "No students or courses available. Press key...")
        stdscr.getch()
        return

    try:
        c_id = get_input(stdscr, 2, 0, "Enter Course ID to grade: ")
        
        # Verify course exists
        selected_course = next((c for c in system.courses if c.id == c_id), None)
        if not selected_course:
            stdscr.addstr(4, 0, "Course not found. Press key...")
            stdscr.getch()
            return

        row = 4
        for student in system.students:
            mark_str = get_input(stdscr, row, 0, f"Mark for {student.name} ({student.id}): ")
            try:
                val = float(mark_str)
                student.add_mark(c_id, val)
            except ValueError:
                pass # Skip invalid inputs
            row += 1
            
        stdscr.addstr(row + 1, 0, "Marks recorded (and rounded). Press key...")
    except Exception as e:
        stdscr.addstr(10, 0, f"Error: {str(e)}")
    
    stdscr.getch()

def list_students_ui(stdscr, system):
    stdscr.clear()
    stdscr.addstr(0, 0, "--- STUDENT LIST (SORTED BY GPA DESC) ---", curses.A_BOLD)
    
    # Calculate and Sort before displaying
    system.sort_students_by_gpa()
    
    if not system.students:
        stdscr.addstr(2, 0, "No students found.")
    else:
        row = 2
        stdscr.addstr(row, 0, f"{'ID':<10} | {'Name':<20} | {'GPA':<5} | {'Marks'}")
        row += 1
        stdscr.addstr(row, 0, "-"*60)
        row += 1
        
        for s in system.students:
            marks_str = ", ".join([f"{k}:{v}" for k,v in s.marks.items()])
            stdscr.addstr(row, 0, f"{s.id:<10} | {s.name:<20} | {s.gpa:<5.2f} | {marks_str}")
            row += 1

    stdscr.addstr(row + 2, 0, "Press any key to return...")
    stdscr.getch()

def main(stdscr):
    # Setup Curses
    curses.curs_set(0) # Hide cursor
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) # For menu selection
    
    system = SchoolManagement()
    
    # Pre-populate some data for testing ease
    # s1 = Student("S01", "Alice", "2000")
    # s2 = Student("S02", "Bob", "2001")
    # c1 = Course("C01", "Math", 3)
    # c2 = Course("C02", "Physics", 4)
    # system.add_student(s1)
    # system.add_student(s2)
    # system.add_course(c1)
    # system.add_course(c2)

    menu_items = ["Add Student", "Add Course", "Input Marks", "Show Student List (GPA Sort)", "Exit"]
    current_row = 0

    while True:
        draw_menu(stdscr, current_row, menu_items)
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu_items) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 0:
                add_student_ui(stdscr, system)
            elif current_row == 1:
                add_course_ui(stdscr, system)
            elif current_row == 2:
                input_marks_ui(stdscr, system)
            elif current_row == 3:
                list_students_ui(stdscr, system)
            elif current_row == 4:
                break

if __name__ == "__main__":
    try:
        wrapper(main)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Note: If you are on Windows, ensure you installed 'windows-curses'")