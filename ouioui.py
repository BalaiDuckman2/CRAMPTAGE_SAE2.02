import random
import pygame

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


def affichage(n):
    pygame.init()
    if n%2==0:
        nbCase = n//2
    else:
        nbCase = n//2+1;
    WIDTH, HEIGHT = 600, 600
    taille_case = 100
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    WHITE = (255, 255, 255)
    BLACK = (118, 118, 118)
    def draw_grid():
        for i in range(0, n):
            if i%2 == 0:
                for j in range(0,nbCase):
                    pygame.draw.rect(screen, BLACK, [200*j+30, 100*i+30, taille_case, taille_case])
            else:
                for j in range(0, nbCase-1):
                    pygame.draw.rect(screen, BLACK, [200*j+130, 100*i+30, taille_case, taille_case])
        pygame.draw.rect(screen, (0,0,0), [30,30, taille_case*n, taille_case*n], 1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        draw_grid()
        pygame.display.flip()

n = 5
affichage(n)