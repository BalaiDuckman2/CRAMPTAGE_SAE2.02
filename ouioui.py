import random

def graphe(n):
    graph = dict()
    for k in range(n*n) :
        i = k//n # ligne de la case k
        j = k%n # colonne de la case k

        graph[k] = []

        if  0 <= i-2 < n and  0 <= j-1 < n :
            graph[k].append((i-2)*n+(j-1))
        if  0 <= i-2 < n and  0 <= j+1 < n :
            graph[k].append((i-2)*n+(j+1))
        if  0 <= i+2 < n and  0 <= j-1 < n :
            graph[k].append((i+2)*n+(j-1))
        if  0 <= i+2 < n and  0 <= j+1 < n :
            graph[k].append((i+2)*n+(j+1))

        if  0 <= i-1 < n and  0 <= j-2 < n :
            graph[k].append((i-1)*n+(j-2))
        if  0 <= i-1 < n and  0 <= j+2 < n :
            graph[k].append((i-1)*n+(j+2))
        if  0 <= i+1 < n and  0 <= j-2 < n :
            graph[k].append((i+1)*n+(j-2))
        if  0 <= i+1 < n and  0 <= j+2 < n :
            graph[k].append((i+1)*n+(j+2))
    return graph


def cavalier(n):
    g = graphe(n)
    chemins = []
    def parcoursCavalier(case, chemin):
        chemin.append(case)
        if len(chemin)==n*n:
            chemins.append(chemin.copy())
        else:
            voisins = []
            for i in g[case]:
                 if i not in chemin:
                      voisins.append(i)
            for v in voisins:
                if parcoursCavalier(v, chemin):
                    chemins.append(chemin)
                else:
                    chemin.pop()
    case1 = random.randint(0,n*n-1)
    parcoursCavalier(case1, [])
    return chemins


def affichage(n, chemins):
    for chemin in chemins:
        t = [[0 for j in range(n) ] for k in range(n)]
        rg = 1
        for x in chemin :
            if rg > 9 :
                t[x//n][x%n] = str(rg)
            else :
                t[x//n][x%n] = '0' + str(rg)
            rg += 1
        for ligne in t :
            for c in ligne :
                print(c, end=" ")
            print()
        print()
    print(len(chemins))

n = 5
chemins = cavalier(n)
affichage(n, chemins)