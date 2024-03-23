import random
import pygame
from pygame.locals import *

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
    return chemins, case1


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
        text = font.render("Nombre de chemin total pour la case "+ str(c) + " : "+ str(len(chemin)), True, (255, 255, 255))
        ecran.blit(text, (25, n*170))
        pygame.display.flip()
        

    else:
        font = pygame.font.SysFont('arial', 35)
        text = font.render("0 chemin possible pour la case :" + str(c), True, (255, 255, 255))
        ecran.blit(text, (25, 80))
        pygame.display.flip()
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()
    """pygame.init()
    WIDTH, HEIGHT = 800, 600
    taille_case = 100
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    WHITE = (255, 255, 255)
    BLACK = (118, 118, 118)
    cord_x = []
    cord_y = []
    for i in range(0, n):
        cord_y.append(100*i+30)
        cord_x.append(100*i+30)
    def draw_grid():
        for i in range(n):
            if i%2==0:
                for j in range(n):
                    if j%2==0:
                        pygame.draw.rect(screen, WHITE, [cord_x[j], cord_y[i], taille_case, taille_case])
                    else:
                        pygame.draw.rect(screen, BLACK, [cord_x[j], cord_y[i], taille_case, taille_case])
            else:
                for j in range(n):
                    if j%2==0:
                        pygame.draw.rect(screen, BLACK, [cord_x[j], cord_y[i], taille_case, taille_case])
                    else:
                        pygame.draw.rect(screen, WHITE, [cord_x[j], cord_y[i], taille_case, taille_case])
        pygame.draw.rect(screen, (0,0,0), [30,30, taille_case*n, taille_case*n], 1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in cord_x:
                    for y in cord_y:
                        if pygame.mouse.get_pos() < (x + taille_case, y + taille_case) and pygame.get_pos()[0] > (x, y):
                            pygame.draw.rect(screen, BLACK, [cord_x[x], cord_y[y], taille_case, taille_case], 5)
        screen.fill((255, 255, 255))
        draw_grid()
        pygame.display.flip()"""
                        

n = 5
chemin, case = cavalier(n)
affichage(n, chemin, case)