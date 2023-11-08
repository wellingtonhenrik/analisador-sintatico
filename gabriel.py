import numpy as np

tabParsing = [[0 for _ in range(45)] for _ in range(73)]

tabParsing[45][8] = 1
tabParsing[46][2] = 2 #
tabParsing[46][21] = 2
tabParsing[46][44] = 2
tabParsing[47][22] = 20
tabParsing[48][21] = 3
tabParsing[48][2] = 4 #
tabParsing[48][44] = 4
tabParsing[49][2] = 5
tabParsing[50][9] = 14
tabParsing[50][44] = 15
tabParsing[50][22] = 15 #
tabParsing[51][1] = 21
tabParsing[51][7] = 21
tabParsing[51][10] = 21 #
tabParsing[51][15] = 21
tabParsing[51][16] = 21
tabParsing[51][17] = 21
tabParsing[51][44] = 22
tabParsing[51][18] = 22 #
tabParsing[52][16] = 6
tabParsing[53][5] = 13
tabParsing[53][6] = 12
tabParsing[53][14] = 11
tabParsing[54][16] = 9
tabParsing[54][44] = 10
tabParsing[54][9] = 10 # 
tabParsing[54][22] = 10 # 
tabParsing[55][36] = 8
tabParsing[55][44] = 7
tabParsing[55][33] = 7 # 
tabParsing[56][39] = 16
tabParsing[56][44] = 17
tabParsing[56][31] = 17 #
tabParsing[57][36] = 18
tabParsing[57][44] = 19
tabParsing[57][38] = 19
tabParsing[58][1] = 78
tabParsing[58][7] = 79
tabParsing[58][10] = 23
tabParsing[58][15] = 24
tabParsing[58][16] = 65
tabParsing[58][17] = 66
tabParsing[59][11] = 39
tabParsing[59][12] = 39
tabParsing[59][13] = 39
tabParsing[59][16] = 39
tabParsing[59][23] = 39
tabParsing[59][39] = 39
tabParsing[60][36] = 40
tabParsing[60][44] = 41
tabParsing[60][41] = 41 # 
tabParsing[61][11] = 42
tabParsing[61][12] = 42
tabParsing[61][13] = 42
tabParsing[61][16] = 42
tabParsing[61][23] = 42
tabParsing[61][39] = 42
tabParsing[62][11] = 46
tabParsing[62][12] = 46
tabParsing[62][13] = 46
tabParsing[62][16] = 46
tabParsing[62][23] = 46
tabParsing[62][39] = 46
tabParsing[63][30] = 43
tabParsing[63][42] = 44
tabParsing[63][44] = 45   
tabParsing[63][41] = 45 #
tabParsing[64][11] = 53
tabParsing[64][12] = 52
tabParsing[64][13] = 54
tabParsing[64][16] = 51
tabParsing[64][23] = 55
tabParsing[64][39] = 50
tabParsing[65][34] = 48
tabParsing[65][37] = 47
tabParsing[65][44] = 49
tabParsing[65][41] = 49 #
tabParsing[66][11] = 56
tabParsing[66][12] = 56
tabParsing[66][13] = 56
tabParsing[66][16] = 56
tabParsing[66][23] = 56
tabParsing[66][39] = 56
tabParsing[67][19] = 57
tabParsing[67][44] = 58
tabParsing[68][11] = 60
tabParsing[68][12] = 59
tabParsing[68][13] = 61
tabParsing[68][16] = 58
tabParsing[68][23] = 62
tabParsing[68][39] = 57
tabParsing[69][34] = 63
tabParsing[69][44] = 64
tabParsing[69][31] = 67 #
tabParsing[69][39] = 67 #  
tabParsing[70][11] = 53
tabParsing[70][12] = 52
tabParsing[70][13] = 54
tabParsing[70][16] = 68
tabParsing[70][23] = 55
tabParsing[70][39] = 69 #
tabParsing[71][12] = 72 #
tabParsing[71][30] = 66
tabParsing[71][42] = 66
tabParsing[71][44] = 66 #
tabParsing[72][11] = 53
tabParsing[72][12] = 52
tabParsing[72][13] = 54
tabParsing[72][16] = 74
tabParsing[72][23] = 55
tabParsing[72][38] = 77 # 
tabParsing[72][39] = 73


producoes = [[0 for _ in range(10)] for _ in range(82)]
producoes[1][1] = 8
producoes[1][2] = 16
producoes[1][3] = 31
producoes[1][4] = 46
producoes[1][5] = 47
producoes[1][6] = 35
producoes[2][1] = 48
producoes[2][2] = 49
producoes[2][3] = 50
producoes[3][1] = 21
producoes[3][2] = 16
producoes[3][3] = 26
producoes[3][4] = 12
producoes[3][5] = 31
producoes[3][6] = 48
producoes[4][1] = 44
producoes[5][1] = 2
producoes[5][2] = 52
producoes[5][3] = 33
producoes[5][4] = 53
producoes[5][5] = 31
producoes[5][6] = 54
producoes[6][1] = 16
producoes[6][2] = 55
producoes[7][1] = 44
producoes[8][1] = 36
producoes[8][2] = 16
producoes[8][3] = 55
producoes[9][1] = 52
producoes[9][2] = 33
producoes[9][3] = 53
producoes[9][4] = 31
producoes[9][5] = 54
producoes[10][1] = 44
producoes[11][1] = 14
producoes[12][1] = 6
producoes[13][1] = 5
producoes[14][1] = 9
producoes[14][2] = 16
producoes[14][3] = 56
producoes[14][4] = 31
producoes[14][5] = 47
producoes[14][6] = 31
producoes[14][7] = 50
producoes[15][1] = 44
producoes[16][1] = 39
producoes[16][2] = 52
producoes[16][3] = 33
producoes[16][4] = 53
producoes[16][5] = 57
producoes[16][6] = 38
producoes[17][1] = 44
producoes[18][1] = 36
producoes[18][2] = 52
producoes[18][3] = 33
producoes[18][4] = 53
producoes[18][5] = 57
producoes[19][1] = 44
producoes[20][1] = 22
producoes[20][2] = 51
producoes[20][3] = 18
producoes[21][1] = 58
producoes[21][2] = 31
producoes[21][3] = 51
producoes[22][1] = 44
producoes[23][1] = 10
producoes[23][2] = 38
producoes[23][3] = 59
producoes[23][4] = 60
producoes[23][5] = 39
producoes[24][1] = 15
producoes[24][2] = 66
producoes[24][3] = 4
producoes[24][4] = 47
producoes[24][5] = 67
producoes[25][1] = 16
producoes[25][2] = 69
producoes[26][1] = 17
producoes[26][2] = 16
producoes[26][3] = 32
producoes[26][4] = 61
producoes[26][5] = 3
producoes[26][6] = 61
producoes[26][7] = 20
producoes[26][8] = 47
producoes[27][1] = 1
producoes[27][2] = 66
producoes[27][3] = 20
producoes[27][4] = 47
producoes[28][1] = 7
producoes[28][2] = 39
producoes[28][3] = 16
producoes[28][4] = 38
producoes[29][1] = 70
producoes[30][1] = 32
producoes[30][2] = 61
producoes[31][1] = 39
producoes[31][2] = 71
producoes[31][3] = 72
producoes[31][4] = 38
producoes[32][1] = 44
producoes[33][1] = 16
producoes[34][1] = 12
producoes[35][1] = 11
producoes[36][1] = 23
producoes[37][1] = 36
producoes[37][2] = 71
producoes[37][3] = 72
producoes[38][1] = 44
producoes[39][1] = 61
producoes[40][1] = 36
producoes[40][2] = 59
producoes[40][3] = 60
producoes[41][1] = 44
producoes[42][1] = 62
producoes[42][2] = 63
producoes[43][1] = 30
producoes[43][2] = 62
producoes[43][3] = 63
producoes[44][1] = 42
producoes[44][2] = 62
producoes[44][3] = 63
producoes[45][1] = 44
producoes[46][1] = 64
producoes[46][2] = 65
producoes[47][1] = 37
producoes[47][2] = 64
producoes[47][3] = 65
producoes[48][1] = 34
producoes[48][2] = 64
producoes[48][3] = 65
producoes[49][1] = 44
producoes[50][1] = 39
producoes[50][2] = 61
producoes[50][3] = 38
producoes[51][1] = 16
producoes[52][1] = 12
producoes[53][1] = 11
producoes[54][1] = 13
producoes[55][1] = 23
producoes[56][1] = 61
producoes[56][2] = 68
producoes[56][3] = 61
producoes[57][1] = 26
producoes[58][1] = 27
producoes[59][1] = 29
producoes[60][1] = 25
producoes[61][1] = 28
producoes[62][1] = 24
producoes[63][1] = 19
producoes[63][2] = 47
producoes[64][1] = 44
producoes[65][1] = 16
producoes[65][2] = 69
producoes[66][1] = 17
producoes[66][2] = 16
producoes[66][3] = 32
producoes[66][4] = 61
producoes[66][5] = 3
producoes[66][6] = 61
producoes[66][7] = 20
producoes[66][8] = 47
producoes[67][1] = 70
producoes[68][1] = 32
producoes[68][2] = 61
producoes[69][1] = 39
producoes[69][2] = 71
producoes[69][3] = 72
producoes[69][4] = 38
producoes[70][1] = 44
producoes[71][1] = 16
producoes[72][1] = 12
producoes[73][1] = 11
producoes[74][1] = 23
producoes[75][1] = 13
producoes[76][1] = 36
producoes[76][2] = 71
producoes[76][3] = 72
producoes[77][1] = 44
producoes[78][1] = 1
producoes[78][2] = 66
producoes[78][3] = 20
producoes[78][4] = 47
producoes[79][1] = 7
producoes[79][2] = 39
producoes[79][3] = 16
producoes[79][4] = 38

# for i in range(73):
#     for j in range(45):
#         if tabParsing[i][j] != 0:
#             print(f"({i}, {j}): {tabParsing[i][j]}")

# for i in range(1, 81):
#     for j in range(1, 7):
#         if producoes[i][j] != 0:
#             print(f"({i}, {j}): {producoes[i][j]}")

# Tokens virão do analisador léxico
#tokens = [8, 16, 31, 2, 16, 33, 14, 31, 22, 18, 35]
tokens = [8,16,31,21,16,26,12,31,21,16,26,12,31,2,16,33,14,31,9,16,39,16,33,14,38,31,22,10,40,13,41,31,18,31,22,16,39,12,38,31,18,35]
#tokens = [8,16,31,21,16,26,12,31,21,16,26,12,31,2,16,33,14,31,9,16,39,16,33,14,38,31,22,10,40,13,41,31,18,31,22,18,35]


print(tokens) 
tokens = np.array(tokens)

pilha = [43] #$ topo da pilha = gramatica

pilha = np.hstack([producoes[1][:], pilha])
pilha = pilha[pilha != 0]

print(pilha)

X = pilha[0]
a = tokens[0]

while X != 43: #enquanto pilha nao estiver vazia
    print(X)
    print(a)
    print(pilha)
    if X == 44: #se o topo da pilha for vazio
        pilha = np.delete(pilha,[0])
        X = pilha[0]
    else:
        if X <= 44: #topo da pilha eh um terminal
            if X == a: #deu match
                pilha = np.delete(pilha,[0])
                tokens = np.delete(tokens,[0])
                X = pilha[0]
                if tokens.size != 0:
                    a = tokens[0]
            else:
                print('Error, mismatch')
                break
        else: 
            if int(tabParsing[X][a]) != 0: # se existe uma producao
                print('producao: '+str(tabParsing[X][a]))    
                pilha = np.delete(pilha,[0])
                pilha = np.hstack([producoes[int(tabParsing[X][a])][:], pilha]) #empilha as producoes correspondentes
                pilha = pilha[pilha != 0]  
                X = pilha[0]
            else:
                print('Error, no production')
                break
