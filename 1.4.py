import math
with open("input.txt", "r") as file:
    for line in file:
        a, b, c = map(float, line.split())
        
        d = b**2 - 4*a*c

        print(f"\nFor coefficients: a={a}, b={b}, c={c}")
        
        if d >= 0:
            root1 = (-b + math.sqrt(d)) / (2*a)
            root2 = (-b - math.sqrt(d)) / (2*a)

            print("Root 1:", root1)
            print("Root 2:", root2)
        else:
  
            print("No real roots")
