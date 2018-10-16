import math
NuRad = int(input("Enter the max radius:"))
#RadA = math.pi*pow(NuRad,2)
print("Radius Area of circle")

for i in range(1, NuRad+1):
    print(i, math.pi*i*i)
    
