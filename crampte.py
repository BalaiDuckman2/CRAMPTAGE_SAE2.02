import random

def graphe(n) :

    E = dict()
    for k in range(n*n) :
        i = k//n # ligne de la case k
        j = k%n # colonne de la case k

        E[k] = [] # E[k]  : liste des voisins de la case k
        if  0 <= i-2 < n and  0 <= j-1 < n :
            E[k].append((i-2)*n+(j-1))
        if  0 <= i-2 < n and  0 <= j+1 < n :
            E[k].append((i-2)*n+(j+1))
        if  0 <= i+2 < n and  0 <= j-1 < n :
            E[k].append((i+2)*n+(j-1))
        if  0 <= i+2 < n and  0 <= j+1 < n :
            E[k].append((i+2)*n+(j+1))

        if  0 <= i-1 < n and  0 <= j-2 < n :
            E[k].append((i-1)*n+(j-2))
        if  0 <= i-1 < n and  0 <= j+2 < n :
            E[k].append((i-1)*n+(j+2))
        if  0 <= i+1 < n and  0 <= j-2 < n :
            E[k].append((i+1)*n+(j-2))
        if  0 <= i+1 < n and  0 <= j+2 < n :
            E[k].append((i+1)*n+(j+2))
    return E


def cavalierHamilton(n) :
    """ recherche d'un chemin hamiltonien dans le graphe du cavalier."""
    E = graphe(n)
    chemin = [] # contiendra les cases dans leur ordre de visite


    def parcours( case ) :
        """
            case : case actuelle du cavalier.
        """
        chemin.append(case) # case est ajoutée au chemin, ce qui la marque comme visitée également

        if len(chemin) == n*n :
            gagne = True

        else :
            gagne = False
            voisins = [ u for u in E[case] if u not in chemin ] # voisins non visités de case
            for v in voisins :
                if gagne : break
                else : gagne = parcours( v )
            if not gagne :
                chemin.pop() #  case est supprimée de chemin si elle a mené à une impasse

        return gagne

    # départ d'une case prise au hasard :
    parcours(  random.randint(0,n*n-1)  )
    return chemin



def affichage(n) :
	""" affichage simple de l'échiquier avec indication de l'ordre de parcours des cellules réalisé."""

	t = [[0 for j in range(n) ] for k in range(n)]
	chemin = cavalierHamilton(n)

	rg = 1
	for x in chemin :
		if rg > 9 : t[x//n][x%n] = str(rg)
		else : t[x//n][x%n] = '0' + str(rg)
		rg += 1

	for ligne in t :
		for c in ligne :
			print(c, end=" ")
		print()

affichage(6)