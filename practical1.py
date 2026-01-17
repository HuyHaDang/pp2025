# Global lists to store data
students = []
courses = []
marks = []

def input_number_of_students():
    count = int(input("Enter number of students in the class: "))
    return count

def input_student_information():
    print("\n--- Input Student Information ---")
    num = input_number_of_students()
    for _ in range(num):
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dob = input("Enter Student DoB (DD/MM/YYYY): ")
        # Store as a dictionary
        student = {'id': sid, 'name': name, 'dob': dob}
        students.append(student)

def input_number_of_courses():
    count = int(input("Enter number of courses: "))
    return count

def input_course_information():
    print("\n--- Input Course Information ---")
    num = input_number_of_courses()
    for _ in range(num):
        cid = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        course = {'id': cid, 'name': name}
        courses.append(course)

def list_students():
    print("\n--- List of Students ---")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")

def list_courses():
    print("\n--- List of Courses ---")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")

def select_course_and_input_marks():
    print("\n--- Input Marks ---")
    list_courses()
    selected_course_id = input("Enter the ID of the course to input marks for: ")
    
    # Check if course exists
    course_exists = False
    for c in courses:
        if c['id'] == selected_course_id:
            course_exists = True
            break
            
    if not course_exists:
        print("Course not found!")
        return

    for s in students:
        mark = float(input(f"Enter mark for student {s['name']} (ID: {s['id']}): "))
        # Store mark with references to course and student
        data = {
            'course_id': selected_course_id,
            'student_id': s['id'],
            'mark': mark
        }
        marks.append(data)

def show_student_marks_for_course():
    print("\n--- Show Marks ---")
    list_courses()
    selected_course_id = input("Enter the ID of the course to view marks: ")
    
    print(f"\nMarks for Course ID: {selected_course_id}")
    for m in marks:
        if m['course_id'] == selected_course_id:
            # Find student name for better display
            student_name = "Unknown"
            for s in students:
                if s['id'] == m['student_id']:
                    student_name = s['name']
                    break
            print(f"Student: {student_name}, Mark: {m['mark']}")

# Main Menu
def main():
    while True:
        print("\n==============================")
        print("STUDENT MARK MANAGEMENT SYSTEM")
        print("1. Input students")
        print("2. Input courses")
        print("3. List students")
        print("4. List courses")
        print("5. Input marks for a course")
        print("6. Show marks for a course")
        print("0. Exit")
        
        choice = input("Your choice: ")
        
        if choice == '1':
            input_student_information()
        elif choice == '2':
            input_course_information()
        elif choice == '3':
            list_students()
        elif choice == '4':
            list_courses()
        elif choice == '5':
            select_course_and_input_marks()
        elif choice == '6':
            show_student_marks_for_course()
        elif choice == '0':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()