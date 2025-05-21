class Person:
    def __init__(self, id=None, name=None, age=None):
        self._id = id
        self._name = name
        self._age = age

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_id(self, id):
        self._id = id

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def display(self):
        print(f"ID: {self._id}, Name: {self._name}, Age: {self._age}")


class Employee(Person):
    def __init__(self, id=None, name=None, age=None, salary=None):
        super().__init__(id, name, age)
        self._salary = salary

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary

    def compare_salary(self, other):
        if self._salary > other.get_salary():
            print(f"{self.get_name()} has a higher salary than {other.get_name()}.")
        elif self._salary < other.get_salary():
            print(f"{other.get_name()} has a higher salary than {self.get_name()}.")
        else:
            print(f"{self.get_name()} and {other.get_name()} have equal salaries.")

    def display(self):
        super().display()
        print(f"Salary: {self._salary}")


class Manager(Employee):
    def __init__(self, id=None, name=None, age=None, salary=None, department=None):
        super().__init__(id, name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, id=None, name=None, age=None, salary=None, language=None):
        super().__init__(id, name, age, salary)
        self.language = language

    def display(self):
        super().display()
        print(f"Programming Language: {self.language}")


# Storage
person = None
manager = None
developer = None
employees = []  # List to store multiple employees


# Menu logic with match-case
while True:
    print("\nMenu:")
    print("1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Create Developer")
    print("5. Show Details")
    print("6. Compare Salaries by Employee ID")
    print("7. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            person = Person(id, name, age)
            print("Person created successfully.")

        case "2":
            id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = float(input("Enter Salary: "))
            emp = Employee(id, name, age, salary)
            employees.append(emp)
            print("Employee created successfully.")

        case "3":
            id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            manager = Manager(id, name, age, salary, dept)
            print("Manager created successfully.")

        case "4":
            id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = float(input("Enter Salary: "))
            lang = input("Enter Programming Language: ")
            developer = Developer(id, name, age, salary, lang)
            print("Developer created successfully.")

        case "5":
            print("\nDisplay Options:")
            print("a. Person")
            print("b. Employees")
            print("c. Manager")
            print("d. Developer")
            display_choice = input("Choose an option to display: ")

            match display_choice.lower():
                case "a":
                    print("\n--- Person Details ---")
                    if person:
                        person.display()
                    else:
                        print("No Person created.")
                case "b":
                    print("\n--- Employee List ---")
                    if employees:
                        for emp in employees:
                            emp.display()
                            print("---")
                    else:
                        print("No Employees created.")
                case "c":
                    print("\n--- Manager Details ---")
                    if manager:
                        manager.display()
                    else:
                        print("No Manager created.")
                case "d":
                    print("\n--- Developer Details ---")
                    if developer:
                        developer.display()
                    else:
                        print("No Developer created.")
                case _:
                    print("Invalid display option.")

        case "6":
            if len(employees) < 2:
                print("Need at least two employees to compare salaries.")
                continue

            id1 = input("Enter first Employee ID: ")
            id2 = input("Enter second Employee ID: ")

            emp1 = None
            emp2 = None

            for e in employees:
               if e.get_id() == id1:
                  emp1 = e
               if e.get_id() == id2:
                  emp2 = e


            if emp1 and emp2:
                emp1.compare_salary(emp2)
            else:
                print("One or both Employee IDs not found.")

        case "7":
            print("Exiting program.")
            break

        case _:
            print("Invalid choice. Please select from the menu.")
