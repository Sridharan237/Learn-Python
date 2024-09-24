# python program to calculate the salary of a person in which weekly working hours are given in a list

work_hours = [int(x) for x in input('Enter the weekly work hours : ').split()]
hour_salary = int(input('Enter the salary per hour(in rupees) : '))

total_work = 0

for i in range(len(work_hours)):
    total_work += work_hours[i]

week_salary = total_work * hour_salary

print('Total Salary for a person per week : Rs.', week_salary, sep='')


