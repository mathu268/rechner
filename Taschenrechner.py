# Rechenart anfragen
print(" Bitte geben Sie die gewünschte Rechenart an")
print(" Addieren = 1")
print(" Subtrahieren = 2")
print(" Multiplizieren = 3")
print(" Dividieren = 4")
rechenart = input()
x = int(rechenart)
if x == 1:
    print("Geben sie den ersten Summanden ein")
    esummand = int(input())
    print("Geben sie den zweiten Summanden ein")
    zsummand = int(input())
    summe = esummand + zsummand
    print(summe)
elif x == 2:
    print("Geben sie die erste Zahl ein ")
    eZahl = int(input())
    print("Geben sie die zweite Zahl ein ")
    zZahl = int(input())
    diff = eZahl-zZahl
    print(diff)
elif x == 3:
    print("Geben sie die erste Zahl ein")
    eZahl = int(input())
    print("Geben sie die zweite Zahl ein")
    zZahl = int(input())
    produkt = eZahl * zZahl
    print(produkt)
elif x == 4:
    print("Geben sie die erste Zahl ein")
    eZahl = int(input())
    print("Geben sie die zweite Zahl ein")
    zZahl = int(input())
    produkt = eZahl / zZahl
    print(produkt)
else:
    print("Falsche Eingabe")