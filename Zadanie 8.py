import math

a = float(input("Podaj wartość wsółczynnika a: "))
b = float(input("Podaj wartość wsółczynnika b: "))
c = float(input("Podaj wartość wsółczynnika c: "))

if a == 0:
    print ("To nie jest równanie kwadratowe")
else:
    D = b**2 - 4 * a * c

    if D > 0:
        x1 = (-b + math.sqrt(D) / 2*a)
        x2 = (-b - math.sqrt(D) / 2*a)
        print(f"Równanie ma dwa różne pierwiastki: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif D == 0:
        x = - b / 2 * a
        print(f"Równanie ma jeden pierwiastek: x = {x:.2f}")
    else:
        print(f"Równanie nie ma pierwiastków")