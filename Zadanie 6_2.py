import random

droga = random.randint(50, 1000)

spalanie = float(input("Podaj średnie spalanie samochodu: "))
cena_pal = float(input("Podaj aktualną cenę paliwa za litr: "))

zuż_pal = (droga/100) * spalanie
koszt_podr = zuż_pal * cena_pal

print(f"Długość trasy {droga} km")
print(f"Przewidywane zużycie paliwa {zuż_pal:.2f} litrów")
print(f"Szacowany koszt podróży {koszt_podr:.2f} zł")