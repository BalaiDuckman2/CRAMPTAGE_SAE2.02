import random
import pygame


def graphe(n):
    graph = dict()

    for k in range(n*n) :
        i = k//n # ligne de la case k
        j = k%n # colonne de la case k

        graph[k] = [] # graph[k]  : liste des voisins de la case k
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
    chemin = []

    def parcoursCavalier(case):
        chemin.append(case)

        if len(chemin)==n*n:
            return chemin
        else:
            voisins = []
            for i in g[case]:
                 if i not in chemin:
                      voisins.append(i)
            for v in voisins:
                if parcoursCavalier(v):
                    return chemin
            chemin.pop()
    
    case1 = random.randint(0, n*n-1)
    parcoursCavalier(case1)
    return chemin


def afficher_chemin(chemin, n):
    pygame.init()
    ecran = pygame.display.set_mode((n*50, n*50))
    pygame.display.set_caption("Chemin du cavalier")

    num = 1
    for case in chemin:
        i, j = case//n, case%n
        pygame.draw.rect(ecran, (255, 255, 255), (j*50, i*50, 50, 50), 1)
        font = pygame.font.SysFont('arial', 20)
        text = font.render(str(num), True, (255, 255, 255))
        ecran.blit(text, (j*50,i*50,50,50))
        pygame.display.flip()
        pygame.time.delay(100)
        num += 1

    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()


n = 5
chemin = cavalier(n)
afficher_chemin(chemin, n)