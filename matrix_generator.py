# -*- coding:1252 -*-
from random import randint
import sys


def matrix_gen(tam):
    Mat = [[0 for i in range(tam)] for j in range(tam)]
    arquivo = open('matrix.txt', 'w')
    for lin in range(0, tam):
        for col in range(0, tam):
            if(lin == col):
                Mat[col][lin] = 0
            elif(Mat[col][lin] != 0):
                Mat[lin][col] = Mat[col][lin]
            else:
                Mat[lin][col] = randint(0, 100)
            # print(f'{Mat[lin][col]}', end=' ')
            arquivo.write(f'{Mat[lin][col]} ')
        # print('')
        arquivo.write('\n')


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        matrix_gen(int(sys.argv[1]))
    else:
        matrix_gen(10)
