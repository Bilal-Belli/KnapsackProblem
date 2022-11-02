def EnterData():
    poidMax = int(input("Donner le poids maximal : "))
    nbObjets = int(input("Donner le nombre des objets : "))
    matriceObjets =[[],[]]
    matriceResultats =[]
    matriceChoix = []
    # remplissage de la table initial des poids et gains
    for x in range(nbObjets):
        matriceObjets[0].append(int(input("Entrer w"+str(x)+" : ")))
        matriceObjets[1].append(int(input("Entrer v"+str(x)+" : ")))
    # affichage de la table initial
    for x in range(nbObjets):
        print(matriceObjets[0][x],matriceObjets[1][x])
    # creation dynamique de la table des solutions
    for x in range(0,nbObjets+2):
        matriceResultats.append([])
        matriceChoix.append(int(0))
    # initialisation des etats
    for x in range(0,poidMax+1):
        matriceResultats[0].append(int(x))
        matriceResultats[1].append(int(0))
    # algorithme dynamique
    for i in range(1,nbObjets+1):
        for c in range(0,poidMax+1):
            if (c>=matriceObjets[0][i-1]):
                matriceResultats[i+1].append(max(matriceResultats[i][c], matriceResultats[i][c-matriceObjets[0][i-1]]+matriceObjets[1][i-1]))
            else:
                matriceResultats[i+1].append(matriceResultats[i][c])
    print("La valeur maximal dans le sac a dos qui respecte la contrainte est :",str(matriceResultats[nbObjets+1][poidMax]))
    
    # print(matriceResultats)
    for x in range(0, nbObjets+2 ):
        for c in range(0,poidMax + 1):
            print('\t'+str(matriceResultats[x][c]),end = ' ')
        print() #pour sauter la ligne

    # for i in range(nbObjets,0,-1):
    i = nbObjets
    if (matriceResultats[i+1][poidMax] == matriceResultats[i][poidMax]):
        matriceChoix[i+1] = 0
        for p in range(nbObjets,0,-1):
            if (matriceResultats[p+1][poidMax] == matriceResultats[p][poidMax]):
                matriceChoix[p+1] = 0
            else:
                matriceChoix[p+1] = 1
                break
        k = matriceResultats[p+1][poidMax] - matriceObjets[1][p-1]
        if (k != 0):
            for j in range(nbObjets-p+2,0,-1):
                # print(k)
                if (k != 0):
                    print(matriceResultats[j][poidMax])
                    if (k == matriceResultats[j][poidMax]):
                        matriceChoix[j] = 1
                        # print(matriceObjets[1][j-2])
                        k = matriceResultats[j][poidMax] - matriceObjets[1][j-2]
                    else:
                        # Automatiquement ils sont croissent (incrementations)
                        if (k > matriceResultats[j][poidMax]):
                            matriceChoix[j+1] = 1
                            # print(matriceResultats[j][poidMax])
                            # print(matriceResultats[j+1][poidMax])
                            k = k - matriceObjets[1][j]
                        else: # k < matriceResultats[j][poidMax]
                            if (matriceChoix[j] != 1):
                                matriceChoix[j] = 0
                else:
                    break
    else:
        matriceChoix[i+1] = 1
        k = matriceResultats[i+1][poidMax] - matriceObjets[1][i-1]
        if (k != 0):
            for j in range(nbObjets,0,-1):
                if (k != 0):
                    if (k == matriceResultats[j][poidMax]):
                        matriceChoix[j] = 1
                        k = matriceResultats[j][poidMax] - matriceObjets[1][j-1]
                    else:
                        # Automatiquement ils sont croissent (incrementations)
                        if (k > matriceResultats[j][poidMax]):
                            matriceChoix[j+1] = 1
                            k = k - matriceObjets[1][j]
                        else: # k < matriceResultats[j][poidMax]
                            matriceChoix[j] = 0
                else:
                    break
    print(matriceChoix)
    return 0
EnterData()