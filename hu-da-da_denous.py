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

def affichage(n) :
	t = [[0 for j in range(n) ] for k in range(n)]
	chemin = cavalier(n)
	rg = 1
	for x in chemin :
		if rg > 9 : t[x//n][x%n] = str(rg)
		else : t[x//n][x%n] = '0' + str(rg)
		rg += 1
	for ligne in t :
		for c in ligne :
			print(c, end=" ")
		print()

###PYGAME TEST

pygame.init()
screen = pygame.display.set_mode((600, 480))

fond = pygame.image.load("background.jpg").convert()
screen.blit(fond, (0,0))
cava = pygame.image.load("cavalier.png").convert()
screen.blit(cava, (20, 20))

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()