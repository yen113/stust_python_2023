class Employee:

    def __init__ (emp,id,name,salary,department):
        emp.id = id
        emp.name = name
        emp.salary = salary
        emp.department = department

    def calculate_salary(emp,hours_worked):
        if hours_worked > 50 :
            overtime = hours_worked - 50 
            overtime_amount = overtime * (emp.salary / 50)
            return emp.salary + overtime_amount
        else:
            return emp.salary

    def emp_assign_department(emp,new_department):
        emp.department = new_department

    def print_details(emp):
        print(f"Employee ID: {emp.id}")
        print(f"Name: {emp.name}")
        print(f"Salary: {emp.salary}")
        print(f"department: {emp.department}")

emp1 = Employee("E7876", "ADAMS", 50000, "ACCOUNTING")
emp2 = Employee("E7499", "JONES", 45000, "RESEARCH")
emp3 = Employee("E7900", "MARTIN", 50000, "SALES")
emp4 = Employee("E7698", "SMITH", 55000, "OPERATIONS")

print("Original Employee Details:")
emp1.print_details()
emp2.print_details()
emp3.print_details()
emp4.print_details()

emp1.emp_assign_department("OPERATIONS")
emp4.emp_assign_department("SALES")

emp2.calculate_salary(52)
emp4.calculate_salary(60)

print("  ")
print("Updated Employee Details:")
emp1.print_details()
emp2.print_details()
emp3.print_details()
emp4.print_details()