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


def cavalier(n, pos):
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
                        if pygame.mouse.get_pos() < x + taille_case and pygame.get_pos() > x:
                            if pygame.mouse.get_pos() < y + taille_case and pygame.get_pos() > y:
                                
        screen.fill((255, 255, 255))
        draw_grid()
        pygame.display.flip()
        for x in cord_x:
            for y in cord_y:
                if pygame.mouse.get_pos() < (x+x,y+y) and pygame.mouse.get_pos() > (x,y):
                    if pygame.mouse.get_pressed() == True:
                        chemin = cavalier(n)
                        print(chemin[1])
                        

n = 5
affichage(n)