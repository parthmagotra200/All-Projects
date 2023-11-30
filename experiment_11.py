#Write a program that accepts the length of three sides of a triangle as inputs. The program should indicate whether or not the triangle is a right-angled triangle (Use Pythagorean theorem). Also find out its area using Heron's formula.
def is_right_angled(a,b,c):
    sides=[a,b,c]
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("It's a right angled triangle")
    else:
        print("It's not a right angled triangle")
def claculate_area(a,b,c):
#Calculate the area using Heron's formula
    s=(a+b+c)/2
    area =(s*(s-a)*(s-b)*(s-c))**0.5
    print("Area of the triangle: ",area)
# Get input from the user
    side_a = float(int(input("Enter the length of side a: ")))
    side_b = float(int(input("Enter the length of side b: ")))
    side_c = float(int(input("Enter the length of side b: ")))
# Check if it's a right-angled triangle
    is_right_angled(side_a,side_b,side_c)
# Area of triangle usingn Heron's formula
    claculate_area(side_a,side_b,side_c)
