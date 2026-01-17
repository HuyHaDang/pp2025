class Course:
    def __init__(self, name, id, credits):
        self.__name = name
        self.__id = id
        self.__credits = credits

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}, Credits: {self.__credits}"

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_credits(self):
        return self.__credits