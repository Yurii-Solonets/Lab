droga = float(input("Podaj długość trasy: "))
spalanie = float(input("Podaj średnie spalanie samochodu: "))

cena_pal = 6.5

zuż_pal = (droga/100) * spalanie
koszt_pal = zuż_pal * cena_pal

print(f"Przewidywane zużycie paliwa: {zuż_pal:.2f} litrów")
print(f"Szacowany koszt podróży: {koszt_pal:.2f} zł")