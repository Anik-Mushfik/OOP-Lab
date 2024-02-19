with open("D:\Musfique - 0152330101\lab_2\employee_data\emplyee.txt", "r") as file:
    for line in file.readlines():
        emp_data = line.split(",")
        print(emp_data)