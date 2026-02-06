def calc_rectangle(length,width):
    area=length*width

    perimeter=2*(length+width)

    return area, perimeter

#Calling the function

calc_rectangle(3, 4)

#input of length and width

length=int(input("Enter the length:"))

width=int(input("Enter the breadth:"))

#assigning the variables

area, perimeter = calc_rectangle(length, width)

#Printing the value

print(f"The area of rectangle is {perimeter}")

print(f"The area of rectangle is {area}")
