class TabParsing:
    def __init__(self):
        self.tabParsing = [[0 for _ in range(1,46)] for _ in range(1,75)]
        self.producoes = [[0 for _ in range(1,10)] for _ in range(1,82)]

    def inicializarTab(self):
        self.tabParsing = [[0 for _ in range(45)] for _ in range(73)]

        self.tabParsing[45][8] = 1
        self.tabParsing[46][2] = 2
        self.tabParsing[46][21] = 2
        self.tabParsing[47][22] = 20
        self.tabParsing[48][2] = 4
        self.tabParsing[48][21] = 3
        self.tabParsing[49][2] = 5
        self.tabParsing[50][9] = 14
        self.tabParsing[50][22] = 15
        self.tabParsing[51][1] = 21
        self.tabParsing[51][7] = 21
        self.tabParsing[51][10] = 21
        self.tabParsing[51][15] = 21
        self.tabParsing[51][16] = 21
        self.tabParsing[51][17] = 21
        self.tabParsing[51][18] = 22
        self.tabParsing[52][16] = 6
        self.tabParsing[53][5] = 13
        self.tabParsing[53][6] = 12
        self.tabParsing[53][14] = 11
        self.tabParsing[54][9] = 10
        self.tabParsing[54][16] = 9
        self.tabParsing[54][22] = 10
        self.tabParsing[55][33] = 7
        self.tabParsing[55][36] = 8
        self.tabParsing[56][31] = 17
        self.tabParsing[56][39] = 16
        self.tabParsing[57][36] = 18
        self.tabParsing[57][38] = 19
        self.tabParsing[58][1] = 63
        self.tabParsing[58][7] = 64
        self.tabParsing[58][10] = 23
        self.tabParsing[58][15] = 41
        self.tabParsing[58][16] = 51
        self.tabParsing[58][17] = 52
        self.tabParsing[59][11] = 24
        self.tabParsing[59][12] = 24
        self.tabParsing[59][13] = 24
        self.tabParsing[59][16] = 24
        self.tabParsing[59][23] = 24
        self.tabParsing[59][39] = 24
        self.tabParsing[60][36] = 26
        self.tabParsing[60][41] = 25
        self.tabParsing[61][11] = 27
        self.tabParsing[61][12] = 27
        self.tabParsing[61][13] = 27
        self.tabParsing[61][16] = 27
        self.tabParsing[61][23] = 27
        self.tabParsing[61][39] = 27
        self.tabParsing[62][11] = 31
        self.tabParsing[62][12] = 31
        self.tabParsing[62][13] = 31
        self.tabParsing[62][16] = 31
        self.tabParsing[62][23] = 31
        self.tabParsing[62][39] = 31
        self.tabParsing[63][3] = 30
        self.tabParsing[63][4] = 30
        self.tabParsing[63][20] = 30
        self.tabParsing[63][24] = 30
        self.tabParsing[63][25] = 30
        self.tabParsing[63][26] = 30
        self.tabParsing[63][27] = 30
        self.tabParsing[63][28] = 30
        self.tabParsing[63][29] = 30
        self.tabParsing[63][30] = 28
        self.tabParsing[63][31] = 30
        self.tabParsing[63][36] = 30
        self.tabParsing[63][38] = 30
        self.tabParsing[63][41] = 30
        self.tabParsing[63][42] = 29
        self.tabParsing[64][11] = 38
        self.tabParsing[64][12] = 37
        self.tabParsing[64][13] = 39
        self.tabParsing[64][16] = 36
        self.tabParsing[64][23] = 40
        self.tabParsing[64][39] = 35
        self.tabParsing[65][3] = 34
        self.tabParsing[65][4] = 34
        self.tabParsing[65][20] = 34
        self.tabParsing[65][24] = 34
        self.tabParsing[65][25] = 34
        self.tabParsing[65][26] = 34
        self.tabParsing[65][27] = 34
        self.tabParsing[65][28] = 34
        self.tabParsing[65][29] = 34
        self.tabParsing[65][30] = 34
        self.tabParsing[65][31] = 34
        self.tabParsing[65][34] = 33
        self.tabParsing[65][36] = 34
        self.tabParsing[65][37] = 32
        self.tabParsing[65][38] = 34
        self.tabParsing[65][41] = 34
        self.tabParsing[65][42] = 34
        self.tabParsing[66][11] = 42
        self.tabParsing[66][12] = 42
        self.tabParsing[66][13] = 42
        self.tabParsing[66][16] = 42
        self.tabParsing[66][23] = 42
        self.tabParsing[66][39] = 42
        self.tabParsing[67][19] = 49
        self.tabParsing[67][31] = 50
        self.tabParsing[68][24] = 48
        self.tabParsing[68][25] = 46
        self.tabParsing[68][26] = 43
        self.tabParsing[68][27] = 44
        self.tabParsing[68][28] = 47
        self.tabParsing[68][29] = 45
        self.tabParsing[69][31] = 53
        self.tabParsing[69][32] = 54
        self.tabParsing[69][39] = 53
        self.tabParsing[70][31] = 56
        self.tabParsing[70][39] = 55
        self.tabParsing[71][11] = 59
        self.tabParsing[71][12] = 58
        self.tabParsing[71][13] = 65
        self.tabParsing[71][16] = 57
        self.tabParsing[71][23] = 60
        self.tabParsing[72][36] = 61
        self.tabParsing[72][38] = 62

    def inicializarProdu(self):
        self.producoes[1][1] = 8
        self.producoes[1][2] = 16
        self.producoes[1][3] = 31
        self.producoes[1][4] = 46
        self.producoes[1][5] = 47
        self.producoes[1][6] = 35
        self.producoes[2][1] = 48
        self.producoes[2][2] = 49
        self.producoes[2][3] = 50
        self.producoes[3][1] = 21
        self.producoes[3][2] = 16
        self.producoes[3][3] = 26
        self.producoes[3][4] = 12
        self.producoes[3][5] = 31
        self.producoes[3][6] = 48
        self.producoes[4][1] = 44
        self.producoes[5][1] = 2
        self.producoes[5][2] = 52
        self.producoes[5][3] = 33
        self.producoes[5][4] = 53
        self.producoes[5][5] = 31
        self.producoes[5][6] = 54
        self.producoes[6][1] = 16
        self.producoes[6][2] = 55
        self.producoes[7][1] = 44
        self.producoes[8][1] = 36
        self.producoes[8][2] = 16
        self.producoes[8][3] = 55
        self.producoes[9][1] = 52
        self.producoes[9][2] = 33
        self.producoes[9][3] = 53
        self.producoes[9][4] = 31
        self.producoes[9][5] = 54
        self.producoes[10][1] = 44
        self.producoes[11][1] = 14
        self.producoes[12][1] = 6
        self.producoes[13][1] = 5
        self.producoes[14][1] = 9
        self.producoes[14][2] = 16
        self.producoes[14][3] = 56
        self.producoes[14][4] = 31
        self.producoes[14][5] = 47
        self.producoes[14][6] = 31
        self.producoes[14][7] = 50
        self.producoes[15][1] = 44
        self.producoes[16][1] = 39
        self.producoes[16][2] = 52
        self.producoes[16][3] = 33
        self.producoes[16][4] = 53
        self.producoes[16][5] = 57
        self.producoes[16][6] = 38
        self.producoes[17][1] = 44
        self.producoes[18][1] = 36
        self.producoes[18][2] = 52
        self.producoes[18][3] = 33
        self.producoes[18][4] = 53
        self.producoes[18][5] = 57
        self.producoes[19][1] = 44
        self.producoes[20][1] = 22
        self.producoes[20][2] = 51
        self.producoes[20][3] = 18
        self.producoes[21][1] = 58
        self.producoes[21][2] = 31
        self.producoes[21][3] = 51
        self.producoes[22][1] = 44
        self.producoes[23][1] = 10
        self.producoes[23][2] = 40
        self.producoes[23][3] = 59
        self.producoes[23][4] = 60
        self.producoes[23][5] = 41
        self.producoes[24][1] = 15
        self.producoes[24][2] = 66
        self.producoes[24][3] = 4
        self.producoes[24][4] = 47
        self.producoes[24][5] = 67
        self.producoes[25][1] = 16
        self.producoes[25][2] = 69
        self.producoes[26][1] = 17
        self.producoes[26][2] = 16
        self.producoes[26][3] = 32
        self.producoes[26][4] = 61
        self.producoes[26][5] = 3
        self.producoes[26][6] = 61
        self.producoes[26][7] = 20
        self.producoes[26][8] = 47
        self.producoes[27][1] = 1
        self.producoes[27][2] = 66
        self.producoes[27][3] = 20
        self.producoes[27][4] = 47
        self.producoes[28][1] = 7
        self.producoes[28][2] = 39
        self.producoes[28][3] = 16
        self.producoes[28][4] = 38
        self.producoes[29][1] = 70
        self.producoes[30][1] = 32
        self.producoes[30][2] = 61
        self.producoes[31][1] = 39
        self.producoes[31][2] = 71
        self.producoes[31][3] = 72
        self.producoes[31][4] = 38
        self.producoes[32][1] = 44
        self.producoes[33][1] = 16
        self.producoes[34][1] = 12
        self.producoes[35][1] = 11
        self.producoes[36][1] = 23
        self.producoes[37][1] = 36
        self.producoes[37][2] = 71
        self.producoes[37][3] = 72
        self.producoes[38][1] = 44
        self.producoes[39][1] = 61
        self.producoes[40][1] = 36
        self.producoes[40][2] = 59
        self.producoes[40][3] = 60
        self.producoes[41][1] = 44
        self.producoes[42][1] = 62
        self.producoes[42][2] = 63
        self.producoes[43][1] = 30
        self.producoes[43][2] = 62
        self.producoes[43][3] = 63
        self.producoes[44][1] = 42
        self.producoes[44][2] = 62
        self.producoes[44][3] = 63
        self.producoes[45][1] = 44
        self.producoes[46][1] = 64
        self.producoes[46][2] = 65
        self.producoes[47][1] = 37
        self.producoes[47][2] = 64
        self.producoes[47][3] = 65
        self.producoes[48][1] = 34
        self.producoes[48][2] = 64
        self.producoes[48][3] = 65
        self.producoes[49][1] = 44
        self.producoes[50][1] = 39
        self.producoes[50][2] = 61
        self.producoes[50][3] = 38
        self.producoes[51][1] = 16
        self.producoes[52][1] = 12
        self.producoes[53][1] = 11
        self.producoes[54][1] = 13
        self.producoes[55][1] = 23
        self.producoes[56][1] = 61
        self.producoes[56][2] = 68
        self.producoes[56][3] = 61
        self.producoes[57][1] = 26
        self.producoes[58][1] = 27
        self.producoes[59][1] = 29
        self.producoes[60][1] = 25
        self.producoes[61][1] = 28
        self.producoes[62][1] = 24
        self.producoes[63][1] = 19
        self.producoes[63][2] = 47
        self.producoes[64][1] = 44
        self.producoes[65][1] = 16
        self.producoes[65][2] = 69
        self.producoes[66][1] = 17
        self.producoes[66][2] = 16
        self.producoes[66][3] = 32
        self.producoes[66][4] = 61
        self.producoes[66][5] = 3
        self.producoes[66][6] = 61
        self.producoes[66][7] = 20
        self.producoes[66][8] = 47
        self.producoes[67][1] = 70
        self.producoes[68][1] = 32
        self.producoes[68][2] = 61
        self.producoes[69][1] = 39
        self.producoes[69][2] = 71
        self.producoes[69][3] = 72
        self.producoes[69][4] = 38
        self.producoes[70][1] = 44
        self.producoes[71][1] = 16
        self.producoes[72][1] = 12
        self.producoes[73][1] = 11
        self.producoes[74][1] = 23
        self.producoes[75][1] = 13
        self.producoes[76][1] = 36
        self.producoes[76][2] = 71
        self.producoes[76][3] = 72
        self.producoes[77][1] = 44
        self.producoes[78][1] = 1
        self.producoes[78][2] = 66
        self.producoes[78][3] = 20
        self.producoes[78][4] = 47
        self.producoes[79][1] = 7
        self.producoes[79][2] = 39
        self.producoes[79][3] = 16
        self.producoes[79][4] = 38

    def imprimirTabela(self):
        for i in range(73):
            for j in range(45):
                if self.tabParsing[i][j] != 0:
                    print(f"({i}, {j}): {self.tabParsing[i][j]}")

    def imprimirProducoes(self):
        for i in range(1, 81):
            for j in range(1, 7):
                if self.producoes[i][j] != 0:
                    print(f"({i}, {j}): {self.producoes[i][j]}")