class Employee:
    def __init__(self, emp_id, name, age, salary):  # Use double underscores for init
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):  # Use double underscores for str
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

def sort_employee_data(employee_list, key):
    if key == 1:
        return sorted(employee_list, key=lambda emp: emp.age)
    elif key == 2:
        return sorted(employee_list, key=lambda emp: emp.name)
    elif key == 3:
        return sorted(employee_list, key=lambda emp: emp.salary)
    else:
        return employee_list

def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    print("Employee Table")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    try:
        choice = int(input("Enter sorting parameter (1/2/3): "))
        if choice < 1 or choice > 3:
            raise ValueError("Invalid choice")
    except ValueError:
        print("Invalid input. Please enter a valid choice (1/2/3)")
        return

    sorted_employees = sort_employee_data(employees, choice)

    print("Sorted Employee Data:")
    for employee in sorted_employees:
        print(employee)

if __name__ == "__main__":
    main()
