# python program to implement positional and keyword arguments

# net salary calculator
def net_sal(basic, allowance, deduction):
    net_salary = basic + allowance - deduction
    return net_salary

# Positional Arguments
print('Net Salary :', net_sal(8000,6000,2000))
print('Net Salary :', net_sal(2000,6000,8000))

# Keyword Arguments
print('Net Salary :', net_sal(deduction=2000, allowance=6000, basic=8000))

# print('Net Salary :', net_sal(2000, 6000, allowance=8000))
# TypeError: net_sal() got multiple values for argument 'allowance'

print('Net Salary :', net_sal(2000, deduction=6000, allowance=8000))
