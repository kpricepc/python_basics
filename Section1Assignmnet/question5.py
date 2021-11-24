# Start Question #5
overtime_multiplier = 1.5
wage = float(input("Please input the Employee's Wage: "))
standard_hours = float(input("Please input the Employee's Standard Hours: "))
overtime_hours = float(input("Please input the Employee's Overtime Hours: "))

print("This employee's week pay is $" + str(wage*standard_hours + wage*overtime_hours*overtime_multiplier))