#!/usr/bin/python3.9
# Licence MIT (c) 2022 Stéphane Lassalvy
import matplotlib.pyplot as plt
import numpy as np

def my_Trinome(a, b, c):
    # Etude d'un trinome du second degré pour les élèves de terminale connaissant les nombres complexes
    if a == 0:
        print("La fonction n'est pas une fonction du second degré : Fin.")
    elif a > 0 or a < 0:
        print(f"On considère le trinôme ({a})x^2 + ({b})x + ({c})")
        print()
    if a > 0:
        print("a > 0 : la parabole est convexe, avec les branches tournées vers les y positifs")
    else :
        print("a < 0 : la parabole est concave, avec les branches tournées vers les y négatifs")
    print()
    # Détermination du signe de a
    signeANum = np.sign(a)
    if signeANum == -1 :
       signeAChar = "-"
       moinsSigneAChat = "+"
    else :
        signeAChar = "+"
        moinsSigneAChar = "-"
    # Calcul du discriminant
    delta = b**2 - 4 * a * c
    print(f"le discriminant Delta vaut : {delta}")
    print()
    # Calcul des coordonnées du sommet de la parabole
    Sx = -b / 2 / a
    Sy = -delta / 4 / a
    print("les coordonnées du sommet de la parabole sont:")
    print(f"Sx = {Sx}")
    print(f"Sy = {Sy}")
    print()
    print(f"La droite verticale d'équation x = {Sx} est un axe de symétrie de la parabole")
    print()
    # Si le discriminant delta est strictement positif
    if delta > 0:
        print("Delta est strictement positif:")
        print("Il y a deux racines réelles distinctes x1 et x2.")
        x1 = (-b - np.sqrt(delta)) / 2 / a
        x2 = (-b + np.sqrt(delta)) / 2 / a
        print("Le trinôme se factorise sous la forme :")
        print("T(x) = a(x - x1)(x - x2)")
        print(f"a  = {a}")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
        print("La parabole coupe l'axe des abscisses deux points distincts d'abscisses respectives x1 et x2.")
        print()
        # Signe du trinôme
        print("Signe du trinôme : ")
        print("Le trinôme est du signe de a à l'extérieur des racines,")
        print("et du signe de -a entre les racines :")
        print("x    | -Inf  x1    x2  +Inf |")
        print("-----------------------------")
        print(f"T(x) |   {signeAChar}    0  {moinsSigneAChar}  0    {signeAChar}  |")
    # Si delta est nul
    elif delta == 0:
        print("Delta est nul :")
        print("Il y a une racine réelle double x0 :")
        x0 = -b / 2 / a
        print("Le trinôme se factorise sous la forme :")
        print("T(x) = a(x - x0)^2")
        print(f"a  = {a}")
        print(f"x0 = {x0}")
        print()
        print("La parabole coupe l'axe des abscisses en un seul point d'abscisse x0.")
        print()
        #Signe du trinôme
        print("Signe du trinôme : ")
        print("Le trinôme est toujours du signe de a :")
        print("x    | -Inf   x0   +Inf |")
        print("-------------------------")
        print(f"T(x) |    {signeAChar}    0      {signeAChar} |")
    # Si delta est strictement négatif
    elif delta < 0:
        print("Delta est strictement négatif :")
        print("Pas de racines réelles et pas de factorisation dans R.")
        print("La parabole ne coupe pas l'axe des abscisses.")
        #Signe du trinôme
        print("Signe du trinôme : ")
        print("Le trinôme est toujours du signe de a :")
        print("x    | -Inf       +Inf |")
        print("-----------------------")
        print(f"T(x) |       {signeAChar}        |")
        print()
    # Courbe représentative de la fonction trinôme
    lx = np.linspace(Sx - 10,  Sx + 10, 50)
    ly = a*lx ** 2 + b*lx + c
    plt.xlabel('Axe des abscisses')  # étiquette sur l'axe horizontal
    plt.ylabel('Axe des ordonnées')  # étiquette sur l'axe vertical
    plt.axhline(color = 'k')  # tracé de l'axe Ox
    plt.axvline(color = 'k')  # tracé de l'axe Oy
    plt.title("Courbe représentative du Trinôme du second degré")
    plt.plot(lx, ly)
    print("Fermez si besoin la fenêtre graphique pour terminer le programme")
    plt.show()
    print("Fin")
# Saisie des coefficients du trinôme
print("Etude du trinôme du second degré T(x) = ax²+bx+c avec a non nul :")
a = input("Entrez le coefficient a : ")
b = input("Entrez le coefficient b : ")
c = input("Entrez le coefficient c : ")
# Conversion des réponses alphanumériques en numériques (réels)
a = float(a)
b = float(b)
c = float(c)
# Exécution de la fonction _my_Trinome_Term
my_Trinome(a, b, c)
