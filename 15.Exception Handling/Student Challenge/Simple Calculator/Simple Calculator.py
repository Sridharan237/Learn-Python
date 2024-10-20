# python program to implement a simple calculator performs 4 basic arithmetic operations(+, -, *, /) and only takes a expression with (1-operand 1-operator 1-operand) and raise custom exception (InvalidExpressionException) if expression is invalid

# class for InvalidExpressionException
class InvalidExpressionException(Exception):
    pass

# function that evaluates a valid expression and returns result (or) raises Exception if expression is invalid
def evaluate(expression):
    L = expression.split()
    
    if L[1] in '+-*/' and len(L) == 3:
        n1 = int(L[0])
        n2 = int(L[2])
        operator = L[1]
        
        match operator:
            case '+':
                return n1 + n2
            case '-':
                return n1 - n2
            case '*':
                return n1 * n2
            case '/':
                return n1 / n2
    else:
        raise InvalidExpressionException('Expression should be in this form (eg: 10 + 5)')
    
# main Function (or) main part of the program
try:
    expression = input('Enter an expression in this form (eg: 10 + 5) : ')

    print('Result :', evaluate(expression))

except InvalidExpressionException as error:
    print('Error Message :', error)
