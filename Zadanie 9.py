x1 = float(input("Podaj pierwszą liczbę: "))
x2 = float(input(("Podaj drugą liczbę: ")))

dodaw = x1 + x2
odejm = x1 - x2
mnoż = x1 * x2
if x2 != 0:
    dziel = x1 / x2
else:
    dziel = "Nie można dzielić przez zero"
potęg = x1 ** x2

print(f"Wynik dodawania: {dodaw}")
print(f"Wynik odejmowania: {odejm}")
print(f"Wynik mnożenia: {mnoż}")
print(f"Wynik dzielenia: {dziel}")
print(f"Wynik potęgowania: {potęg}")