def graphe(n):
    graph = dict()
    for i in range(n*n):
        lig = i/n
        col = i%n
        #Coup à gauche
        if lig - 2 >= 0 and:
            graph[i].append(i-2-n)
        if i-2+n >=0 and i-2+n <= n*n:
            graph[i].append(i-2+n)
        #Coup en haut
        if i-(n*2)-1 >= 0 and i-(n*2)-1 <= n*n:
            graph[i].append(i-(n*2)-1)
        if i-(n*2)+1 >= 0 and i-(n*2)+1 <= n*n:
            graph[i].append(i-(n*2)+1)
        #Coup en bas
        if i+(n*2)-1 >= 0 and i+(n*2)-1 <= n*n:
            graph[i].append(i+(n*2)-1)
        if i+(n*2)+1 >= 0 and i+(n*2)+1 <= n*n:
            graph[i].append(i+(n*2)+1)
        #Coup à droite