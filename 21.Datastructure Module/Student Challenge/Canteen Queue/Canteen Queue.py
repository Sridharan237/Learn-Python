# python program to implement the function for serving a meal(serve) in a canteen in a queue format

from collections import deque

# object of deque - students - list of students waiting in cateen in a queue format - it contains list of roll numbers of students in order
students = deque([x for x in range(1, 11)])

# function for serving a meal(serve) in a canteen in a queue format
def serve_meal():
    first = students[0] # first student waiting for food in the meal
    
    print('Students in order :', students)
    students.rotate(-1) # -1 to rotate 1 element from left to right (and +1 to rotate 1 element from right to left)
    
    while students[0] != first:
        print('Students in order :', students)
        students.rotate(-1) # -1 to rotate 1 element from left to right



# main part of the program (or) main block
print('Meal Serving : Breakfast')
serve_meal() # serving breakfast

print('Meal Serving : Lunch')
serve_meal() # serving lunch

print('Meal Serving : Dinner')
serve_meal() # serving dinner