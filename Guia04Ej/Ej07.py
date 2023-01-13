matriz = [[1, 5, 1],
          [2, 1, 2],
          [3, 0, 1],
          [1, 4, 4]]

matriz[0].append(matriz[0][0]+matriz[0][1]+matriz[0][2])
matriz[1].append(sum(matriz[1]))
matriz[2] += [sum(matriz[2])]


print(matriz)
