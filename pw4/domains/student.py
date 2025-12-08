import numpy as np

class Student:
    def __init__(self, name, id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
        self.__gpa = 0.0
        # Internal lists for calculation
        self.__marks = []
        self.__credits = []

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_dob(self):
        return self.__dob
    
    def get_gpa(self):
        return self.__gpa

    # Fixed: Pass marks_dict and courses_list as arguments
    def calculateGPA(self, marks_dict, courses_list):
        self.__marks = []
        self.__credits = []
        
        for course in courses_list:
            # Key format must match what you save in input.py
            key = (self.get_id(), course.get_name())
            
            if key in marks_dict:
                self.__credits.append(course.get_credits())
                self.__marks.append(marks_dict[key])
        
        # Avoid division by zero
        if not self.__credits:
            self.__gpa = 0.0
            return

        np_marks = np.array(self.__marks)
        np_credits = np.array(self.__credits)
        
        sumNumpy = np.sum(np_marks * np_credits)
        self.__gpa = sumNumpy / np.sum(np_credits)

    def __str__(self):
        return f"ID: {self.__id:<10} | Name: {self.__name:<20} | GPA: {self.__gpa:.2f} | DoB: {self.__dob}"