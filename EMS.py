employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Ak', 'age': 20, 'department': 'Hacker', 'salary': 777777},
    103: {'name': 'Dk', 'age': 25, 'department': 'SDE', 'salary': 10000000}
}

def add_employee():
    print("\nAdd Employee ")
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employees:
                print("Employee ID already exists. Please enter a unique ID.")
            else:
                break
        except ValueError:
            print("Invalid input. Employee ID must be a number.")

    name = input("Enter Employee Name: ")
    while True:
        try:
            age = int(input("Enter Employee Age: "))
            break
        except ValueError:
            print("Invalid input. Age must be a number.")

    department = input("Enter Employee Department: ")
    while True:
        try:
            salary = float(input("Enter Employee Salary: "))
            break
        except ValueError:
            print("Invalid input. Salary must be a number.")

    employees[emp_id] = {'name': name, 'age': age, 'department': department, 'salary': salary}
    print(f"Employee {name} with ID {emp_id} was successfully added.")

def view_employees():
    print("\nView All Employees ")
    if not employees:
        print("No employees available.")
        return

    print(f"{'ID':<5} {'Name':<15} {'Age':<5} {'Department':<15} {'Salary':<10}")
    print("-" * 60)
    for emp_id, details in employees.items():
        print(f"{emp_id:<5} {details['name']:<15} {details['age']:<5} {details['department']:<15} {details['salary']:<10.2f}")

def search_employee():
    print("\nSearch for Employee ")
    try:
        emp_id = int(input("Enter the Employee ID to search: "))
        if emp_id in employees:
            details = employees[emp_id]
            print(f"\nEmployee Found:")
            print(f"ID: {emp_id}")
            print(f"Name: {details['name']}")
            print(f"Age: {details['age']}")
            print(f"Department: {details['department']}")
            print(f"Salary: {details['salary']:.2f}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input. Employee ID must be a number.")

def main_menu():
    while True:
        print("\nEmployee Management System ")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()