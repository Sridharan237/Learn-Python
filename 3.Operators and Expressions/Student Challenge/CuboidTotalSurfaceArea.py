# python program to find the (TSA)Total Surface Area of a cuboid

length = float(input('Enter length of cuboid : '))
breadth = float(input('Enter breadth of cuboid : '))
height = float(input('Enter height of cuboid : '))

total_surface_area = 2*(length*breadth + length*height + breadth*height)

print("Total Surface Area is", total_surface_area)