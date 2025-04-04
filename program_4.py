# Eliya Statema
# 4/4/25
# Employee Class

class Employee:
    def __init__(self, name, ID, department, title):
        self.__name = name
        self.__ID = ID
        self.__department = department
        self.__title = title

    def set_name(self, name):
        self.__name = name
    def set_ID(self, ID):
        self.__ID = ID
    def set_title(self, title):
         self.__title = title
    def set_department(self, department):
         self.__department = department

    def get_name(self):
        return self.__name
    def get_ID(self):
        return self.__ID
    def get_title(self):
        return self.__title
    def get_department(self):
        return self.__department

    def __str__(self):
        return f'''
    Name: {self.__name}
    ID#: {self.__ID}
    Job Title: {self.__title}
    Department: {self.__department}'''

def main():
    employee_1 = Employee("Susan Meyers", 47899, "Accounting", "Vice president")
    employee_2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee_3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    print(f"{employee_1.__str__()}\n{employee_2.__str__()}\n{employee_3}")

if __name__ == "__main__":
    main()