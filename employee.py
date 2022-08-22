# Joe Cooper
# Complete
# Program creates a class called Employee with an __init__ method to initialize the data attributes of the object,
# defines set methods and get methods for each of the attributes and also creates a __str__ method for the current
# state of each object

class Employee:

    def __init__(self, employee_num, name, id_number, department, job_title):
        self.employee_num = employee_num
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def set_employee_num(self, employee_num):
        self.employee_num = employee_num

    def set_name(self, name):
        self.name = name

    def set_id_number(self, id_number):
        self.id_number = id_number

    def set_department(self, department):
        self.department = department

    def set_job_title(self, job_title):
        self.job_title = job_title

    def get_employee_num(self):
        return self.employee_num

    def get_name(self):
        return self.name

    def get_id_number(self):
        return self.id_number

    def get_department(self):
        return self.department

    def get_job_title(self):
        return self.job_title

    def __str__(self):
        return self.employee_num + '\n' + 'Name: ' + self.name + '\n' + 'ID Number: '\
               + self.id_number + '\n' + 'Department: ' + self.department + '\n' + 'Title: ' + self.job_title + '\n' \
               + '\n '
