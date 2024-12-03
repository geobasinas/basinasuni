import cmath

print("--- Kalosorisate sto programma gia ton ypologismo rizon trionomou ---")
print("-- Dvste tis times twn a, b, c gia to trinomo a*x^2 + b*x + c = 0 --")

# Get user input
a = int(input("Dose a: "))
b = int(input("Dose b: "))
c = int(input("Dose c: "))

# Elegje an to a einai 0
if a == 0:
    # Elegje an to b einai 0
    if b == 0:
        # Elegje an to c einai 0
        if c == 0:
            print("H exisosi einai aoristh")
            print("Oloi oi pragmatikoi arithmoi einai rizes")
        else:
            print("H exisosi den exei rizes")
    else:
        x = -c / b
        print("H exisosi exei lysh:", x)
else:
    # Ypologsimos thw diakrinousas
    discriminant = b**2 - 4*a*c
    
    print("Diakrinousa =", discriminant)
    
    # Elegxos thw diakrinousas kai ypologismos twn rizwn
    if discriminant > 0:
        x1 = (-b + (discriminant ** 0.5)) / (2 * a)
        x2 = (-b - (discriminant ** 0.5)) / (2 * a)
        print("H exisosi exei duo pragmatikes rizes:")
        print("x1 =", x1)
        print("x2 =", x2)
        
        if x1 > x2:
            print("Megalyterh lysh einai:", x1)
        else:
            print("Megalyterh lysh einai:", x2)
            
    elif discriminant == 0:
        x = -b / (2 * a)
        print("h exisosi exei mia pragmatiki riza:")
        print("x =", x)
        
    else:
        x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print("H exisosi den exei pragmatikes rizes alla exei duo fantasitkes rizes:")
        print("x1 =", x1)
        print("x2 =", x2)

print("--- To programma termatise ---")