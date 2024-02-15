employee_dict = {}

while True:
    empName = input("Enter employee name or type 'no' to exit: ")

    if empName == 'no':
        break

    salary_str = input("Enter employee salary: ")

    empSalary = float(salary_str)

    employee_dict[empName] = empSalary

print(employee_dict)
