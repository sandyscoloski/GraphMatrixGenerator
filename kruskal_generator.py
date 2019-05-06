# -*- coding:1252 -*-


def kruskal_gen(Mat):
    i = 0
    arquivo = open('kruskal.txt', 'w')
    for lin in range(0, len(Mat)):
        for col in range(0, len(Mat[lin])):
            if(Mat[lin][col] != 0 and col > lin):
                arquivo.write(f'{lin} {col} {Mat[lin][col]}\n')
                i += 1


if __name__ == '__main__':
    lin = 0
    arquivo = open('matrix.txt', 'r')
    read = arquivo.readlines()
    tam = len(read)
    mat = [[0 for i in range(tam)] for j in range(tam)]
    for val in read:
        val = val.split('\n')
        val = val[0]
        val = val.split(' ')
        for col in range(0, tam):
            mat[lin][col] = int(val[col])
        lin += 1
    # print(f'{mat}')
    kruskal_gen(mat)
