def meilleur_cafe():
    choix = [
        # (nom , distance en km , qualite sur 10)
        (" Starbucks ", 1.2, 8),
        (" Cafe ␣ local ", 0.5, 7),
        (" Pete ’s ␣ Coffee ", 1.8, 9),
        (" Dunkin ’␣ Donuts ", 0.8, 6)
    ]

    meilleur_choix = None
    ratio_distance = 10

    for i in range(0, len(choix)):
        for j in range(1, len(choix[i])):
            #print(choix[i][j], end=" ")
            cote = choix[i][1] * ratio_distance + choix[i][2]
            if cote



if __name__ == "__main__":

    meilleur_cafe()
