# -*- coding:1252 -*-


def kruskal_gen(Mat):
    i = 0
    arquivo = open('kruskal.txt', 'w')
    for lin in range(0, len(Mat)):
        for col in range(0, len(Mat[lin])):
            if(Mat[lin][col] != 0 and col > lin):
                arquivo.write(f'{lin} {col} {Mat[lin][col]}\n')
                # arquivo.write('\n')
                i += 1
            # print(f'{Mat[lin][col]}', end=' ')
            # arquivo.write(f'{Mat[lin][col]}, ')
        # print('')


if __name__ == '__main__':
    lin = 0
    arquivo = open('matrix.txt', 'r')
    read = arquivo.readlines()
    tam = len(read)
    mat = [[0 for i in range(tam)] for j in range(tam)]
    print(f'{tam}')
    for val in read:
        val = val.split('\n')
        val = val[0]
        val = val.split(' ')
        for col in range(0, tam):
            mat[lin][col] = int(val[col])
        lin += 1
    # print(f'{mat}')
    kruskal_gen(mat)

# mat = ((0, 2, 0, 6, 0),
#        (2, 0, 3, 8, 5),
#        (0, 3, 0, 0, 7),
#        (6, 8, 0, 0, 9),
#        (0, 5, 7, 9, 0))

# arquivo.write(f'graph->edge[{i}].src = {lin};\n')
# arquivo.write(f'graph->edge[{i}].dest = {col};\n')
# arquivo.write(f'graph->edge[{i}].weight = {Mat[lin][col]};\n')
