choix = [
        # (nom , distance en km , qualite sur 10)
        (" Starbucks ", 1.2, 8),
        (" Cafe ␣ local ", 0.5, 7),
        (" Pete ’s ␣ Coffee ", 1.8, 9),
        (" Dunkin ’␣ Donuts ", 0.8, 6)
    ]

def meilleur_cafe(choix):

    meilleur_choix = []
    RATIO_DISTANCE = 10
    IND_NOM = 0
    IND_DISTANCE = 1
    IND_QUALITE = 2


    for i in range(0, len(choix)):
        cote = choix[i][IND_DISTANCE] * RATIO_DISTANCE + choix[i][IND_QUALITE]
        meilleur_choix.append(cote)

    print(f' Le ␣ meilleur ␣ cafe ␣ est ␣ {choix[meilleur_choix.index(max(meilleur_choix))][IND_NOM]}. ')

meilleur_cafe(choix)


class Cafe:
    def __init__(self, nom, distance, qualite):
        self.nom = nom
        self.distance = distance
        self.qualite = qualite
        if distance == 0 or distance < 1:
            distance = 0.1
        if distance > 15:
            distance = 1
            qualite = 0
        self.score = qualite / distance

    def __str__(self):
        return f"{self.nom} est à {self.distance} km et a une qualité de {self.qualite}."

    def __repr__(self):
        print("Function __rep")
        return f"{self.nom}"

    def __eq__(self, other):
        return self.score >= other.score

liste_cafes = []

for cafe in choix:
    liste_cafes.append(Cafe(cafe[0], cafe[1], cafe[2]))

liste_cafes.sort(key=lambda x: x.score, reverse=True)

print(liste_cafes)




