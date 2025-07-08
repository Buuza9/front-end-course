def input_user_date():
    name = input("Enter the employer's name : ")
    salary = int(input("Enter the employer's salary : "))
    return {"name": name, "salary": salary}

employees = []

def calcualte_tax(salary):
    if salary > 5000:
        tax_rate = 0.20
    elif 3000 <= salary <= 5000:
        tax_rate = 0.15
    else:
        tax_rate = 0.10
    tax = salary * tax_rate
    net_salary = salary - tax
    return tax, net_salary


for i in range(3):
    print(f"Enter the information of employer {i + 1}")
    emp = input_user_date()
    tax, net_salary = calcualte_tax(emp["salary"])
    emp["tax"] = tax
    emp["net_salary"] = net_salary
    employees.append(emp)

print("\nEmployee Details")
for emp in employees:
    print(f"---------Employee No. {i + 1} Details-----------")
    print(f"Name: {emp['name']}")
    print(f"Salary: {emp['salary']}")
    print(f"Tax amount: {emp['tax']}")
    print(f"Net salary after tax: {emp['net_salary']}")
