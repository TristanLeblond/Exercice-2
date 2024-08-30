def meilleur_cafe():
    choix = [
        # (nom , distance en km , qualite sur 10)
        (" Starbucks ", 1.2, 8),
        (" Cafe ␣ local ", 0.5, 7),
        (" Pete ’s ␣ Coffee ", 1.8, 9),
        (" Dunkin ’␣ Donuts ", 0.8, 6)
    ]

    meilleur_choix = []
    RATIO_DISTANCE = 10
    IND_NOM = 0
    IND_DISTANCE = 1
    IND_QUALITE = 2


    for i in range(0, len(choix)):
        cote = choix[i][IND_DISTANCE] * RATIO_DISTANCE + choix[i][IND_QUALITE]
        meilleur_choix.append(cote)

    print(f' Le ␣ meilleur ␣ cafe ␣ est ␣ {choix[meilleur_choix.index(max(meilleur_choix))][IND_NOM]}. ')

if __name__ == "__main__":

    meilleur_cafe()
