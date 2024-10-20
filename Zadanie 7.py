a = float(input("Podaj wartość współczynnika a: "))
b = float(input("Podaj wartość współczynnika "))

if a == 0:
    if b == 0:
        print ("Nieskończenie wiele rozwiązań")
    else:
        print ("Brak rozwiązań")
else:
    x = -b/a
    print(f"Rozwiązanie równania to: x = {x:.2f}" )