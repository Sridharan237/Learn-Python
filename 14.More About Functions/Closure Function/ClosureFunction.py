# python program to implement closure function (or) factory function - factory for functions

def closure(msg):   # closure() function - closure or factory function which is producing or returning display function when it is called
    
    def display():
        print('*' * 5)
        print(msg)
        print('*' * 5)
    
    print(display)  # Output : <function closure.<locals>.display at 0x000001F4509DB6A0>
    
    return display

d = closure('hello')

print(d)    # Output : <function closure.<locals>.display at 0x000001F4509DB6A0>
d()