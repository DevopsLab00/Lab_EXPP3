employees = {
    "E001": {"name": "Alice", "age": 30, "salary": 55000},
    "E002": {"name": "Bob", "age": 45, "salary": 75000},
    "E003": {"name": "Charlie", "age": 28, "salary": 48000},
    "E004": {"name": "David", "age": 35, "salary": 62000},
    "E005": {"name": "Eva", "age": 40, "salary": 69000}
}
for emp_id, details in employees.items():
    print(f"Employee ID: {emp_id}")
    print(f"  Name: {details['name']}")
    print(f"  Age: {details['age']}")
    print(f"  Salary: ${details['salary']}")
    print("-" * 30)

employees = {
    "E001": {"name": "Alice", "age": 30, "salary": 55000},
    "E002": {"name": "Bob", "age": 45, "salary": 75000},
    "E003": {"name": "Charlie", "age": 28, "salary": 48000},
    "E004": {"name": "David", "age": 35, "salary": 62000},
    "E005": {"name": "Eva", "age": 40, "salary": 69000}
}
total_salary = 0
for emp_id, details in employees.items():
    print(f"Employee ID: {emp_id}")
    print(f"  Name: {details['name']}")
    print(f"  Age: {details['age']}")
    print(f"  Salary: ${details['salary']}")
    print("-" * 30)
    total_salary += details['salary']  

print(f"Total Salary of all employees: ${total_salary}")

employees = {
    "E001": {"name": "Alice", "age": 30, "salary": 55000},
    "E002": {"name": "Bob", "age": 45, "salary": 75000},
    "E003": {"name": "Charlie", "age": 28, "salary": 48000},
    "E004": {"name": "David", "age": 35, "salary": 62000},
    "E005": {"name": "Eva", "age": 40, "salary": 69000}
}
salaries = [details['salary'] for details in employees.values()]
min_salary = min(salaries)
max_salary = max(salaries)
print(f"Minimum Salary: ${min_salary}")
print(f"Maximum Salary: ${max_salary}")

employees = {
    "E001": {"name": "Alice", "age": 30, "salary": 55000},
    "E002": {"name": "Bob", "age": 45, "salary": 75000},
    "E003": {"name": "Charlie", "age": 28, "salary": 48000},
    "E004": {"name": "David", "age": 35, "salary": 62000},
    "E005": {"name": "Eva", "age": 40, "salary": 69000}
}
highest_salary_employee = max(employees.items(), key=lambda x: x[1]['salary'])
emp_id, details = highest_salary_employee
print(f"Employee with the highest salary:")
print(f"  Employee ID: {emp_id}")
print(f"  Name: {details['name']}")
print(f"  Age: {details['age']}")
print(f"  Salary: ${details['salary']}")

employees = {
    "E001": {"name": "Alice", "age": 30, "salary": 55000},
    "E002": {"name": "Bob", "age": 45, "salary": 75000},
    "E003": {"name": "Charlie", "age": 28, "salary": 48000},
    "E004": {"name": "David", "age": 35, "salary": 62000},
    "E005": {"name": "Eva", "age": 40, "salary": 69000}
}
employees_above_25k = [details['name'] for details in employees.values() if details['salary'] > 25000]
print("Employees with salary greater than 25,000:")
print(", ".join(employees_above_25k))employees = {
    "E001": {"name": "Alice", "age": 30, "salary": 55000},
    "E002": {"name": "Bob", "age": 45, "salary": 75000},
    "E003": {"name": "Charlie", "age": 28, "salary": 48000},
    "E004": {"name": "David", "age": 35, "salary": 62000},
    "E005": {"name": "Eva", "age": 40, "salary": 69000}
}
for emp_id, details in employees.items():
    print(f"Employee ID: {emp_id}")
    print(f"  Name: {details['name']}")
    print(f"  Age: {details['age']}")
    print(f"  Salary: ${details['salary']}")
    print("-" * 30)

employees = {
    "E001": {"name": "Alice", "age": 30, "salary": 55000},
    "E002": {"name": "Bob", "age": 45, "salary": 75000},
    "E003": {"name": "Charlie", "age": 28, "salary": 48000},
    "E004": {"name": "David", "age": 35, "salary": 62000},
    "E005": {"name": "Eva", "age": 40, "salary": 69000}
}
total_salary = 0
for emp_id, details in employees.items():
    print(f"Employee ID: {emp_id}")
    print(f"  Name: {details['name']}")
    print(f"  Age: {details['age']}")
    print(f"  Salary: ${details['salary']}")
    print("-" * 30)
    total_salary += details['salary']  

print(f"Total Salary of all employees: ${total_salary}")

employees = {
    "E001": {"name": "Alice", "age": 30, "salary": 55000},
    "E002": {"name": "Bob", "age": 45, "salary": 75000},
    "E003": {"name": "Charlie", "age": 28, "salary": 48000},
    "E004": {"name": "David", "age": 35, "salary": 62000},
    "E005": {"name": "Eva", "age": 40, "salary": 69000}
}
salaries = [details['salary'] for details in employees.values()]
min_salary = min(salaries)
max_salary = max(salaries)
print(f"Minimum Salary: ${min_salary}")
print(f"Maximum Salary: ${max_salary}")

employees = {
    "E001": {"name": "Alice", "age": 30, "salary": 55000},
    "E002": {"name": "Bob", "age": 45, "salary": 75000},
    "E003": {"name": "Charlie", "age": 28, "salary": 48000},
    "E004": {"name": "David", "age": 35, "salary": 62000},
    "E005": {"name": "Eva", "age": 40, "salary": 69000}
}
highest_salary_employee = max(employees.items(), key=lambda x: x[1]['salary'])
emp_id, details = highest_salary_employee
print(f"Employee with the highest salary:")
print(f"  Employee ID: {emp_id}")
print(f"  Name: {details['name']}")
print(f"  Age: {details['age']}")
print(f"  Salary: ${details['salary']}")

employees = {
    "E001": {"name": "Alice", "age": 30, "salary": 55000},
    "E002": {"name": "Bob", "age": 45, "salary": 75000},
    "E003": {"name": "Charlie", "age": 28, "salary": 48000},
    "E004": {"name": "David", "age": 35, "salary": 62000},
    "E005": {"name": "Eva", "age": 40, "salary": 69000}
}
employees_above_25k = [details['name'] for details in employees.values() if details['salary'] > 25000]
print("Employees with salary greater than 25,000:")
print(", ".join(employees_above_25k))
