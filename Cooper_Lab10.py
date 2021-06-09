# Joe Cooper
# Complete
# Program defines a main function that initiates a list called employee_list, requests input for 5 variables 3 times,
# appends to the list using the index of the list as an object with the variables as attributes to the class Employee
# The program then calls display_list, a function that prints each item added to the list using the __str__ function.


import employee


def main():
    employee_list = []
    for names in range(3):
        employee_num = 'Employee #' + str(names + 1)
        name = input("Enter employee name: ").title()
        id_number = input("Enter employee ID: ")
        department = input("Enter department: ").capitalize()
        job_title = input("Enter position: ").capitalize()

        employee_list.append(employee.Employee(employee_num, name, id_number, department, job_title))

    display_list(employee_list)


def display_list(lst):
    for obj in lst:
        print(obj, '\n')


main()
