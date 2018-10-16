# write a funbction that takes 4 ints representing 2 coordinates in plane & returns the Euclidean distance betwween them
import math

def Distance(x1,y1,x2,y2):
    D = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return D

def main():
    x_1 = float(input("Enter the coordinates X1: "))
    y_1 = float(input("Enter the coordinates Y1: "))
    x_2 = float(input("Enter the coordinates X2: "))
    y_2 = float(input("Enter the coordinates Y2: "))

    Dis = Distance(x_1,y_1,x_2,y_2)

    print("Distance:", Dis)

if _name_ == "_main_":
    main()
