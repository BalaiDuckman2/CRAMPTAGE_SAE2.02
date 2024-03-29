import random
import pygame
from pygame.locals import *

def graphe(n):
    graph = dict()
    for k in range(n*n) :
        i = k//n # ligne de la case k
        j = k%n # colonne de la case k

        graph[k] = []

        #Met dans le graphe toutes les cases possible pour la case k
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
    #Fonction DFS parcours du graphe en profondeur, parcours tous les chemins possible, si la longueur du chemin final
    #est égale à n*n (nombre de case de l'échiquier) le chemin est mis dans une liste qui est retourner a la fin de la boucle
    #Elle retourne également la case de commencement qui est choisis aléatoirement ici
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
    return chemins, case1

#Affichage du parcours du cavalier avec le module pygame, affiche les cases une par un numéro correspondant a l'ordre de passage d'une case
# et affiche le nombre de chemin total pour la case
def affichage(n, chemin, c):
    pygame.init()
    ecran = pygame.display.set_mode((n*150, n*200))
    pygame.display.set_caption("Chemin du cavalier")

    if len(chemin) > 0:
        num = 1
        parcours = chemin[random.randint(0, len(chemin))-1]
        for case in parcours:
            i, j = case//n, case%n
            pygame.draw.rect(ecran, (255, 255, 255), (j*150, i*150, 150, 150), 1)
            font = pygame.font.SysFont('arial', 50)
            text = font.render(str(num), True, (255, 255, 255))
            ecran.blit(text, (j*150,i*150,150,150))
            pygame.display.flip()
            pygame.time.delay(100)
            num += 1
        font = pygame.font.SysFont('arial', 35)
        text = font.render("Nombre de chemin total pour la case "+ str(c + 1) + " : "+ str(len(chemin)), True, (255, 255, 255))
        ecran.blit(text, (25, n*170))
        pygame.display.flip()
        

    else:
        font = pygame.font.SysFont('arial', 35)
        text = font.render("0 chemin possible pour la case :" + str(c + 1), True, (255, 255, 255))
        ecran.blit(text, (25, 80))
        pygame.display.flip()
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()
                        

n = 5
chemin, case = cavalier(n)
affichage(n, chemin, case)