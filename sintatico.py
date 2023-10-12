"""
@author: marlonoliveira

1)     S → cAa 
2)     A → cB 
3)     A → B 
4)     B → bcB
5)     B → î

1 î 
2 c
3 b 
4 a
5 $
6 S
7 A
8 B
"""
import numpy as np

#entrada, geralmente vem de um arquivo texto
palavra = 'cbca'
tokens = [2, 3, 2, 4]

        
print(tokens) 
tokens = np.array(tokens)

producoes = [[2,7,4]] #p1
producoes = np.append(producoes, [[2,8,0]], axis = 0); #P2
producoes = np.append(producoes, [[8,0,0]], axis = 0); #P3
producoes = np.append(producoes, [[3,2,8]], axis = 0); #P4 
producoes = np.append(producoes, [[1,0,0]], axis = 0); #P5

#inicializar a Matriz de Parsing com zeros.
tabParsing = np.zeros((9, 6))
  			
tabParsing[6][2] = 1;
tabParsing[7][2] = 2;
tabParsing[7][3] = 3;
tabParsing[7][4] = 3;
tabParsing[8][3] = 4;
tabParsing[8][4] = 5;

pilha = [5] #$ topo da pilha

pilha = np.hstack([producoes[0][:], pilha])

print(pilha)

X = pilha[0]
a = tokens[0]

while X != 5: #enquanto pilha nao estiver vazia
    print(X)
    print(a)
    print(pilha)
    if X == 1: #se o topo da pilha for vazio
        pilha = np.delete(pilha,[0])
        X = pilha[0]
    else:
        if X <= 5: #topo da pilha eh um terminal
            if X == a: #deu match :D
                pilha = np.delete(pilha,[0])
                tokens = np.delete(tokens,[0])
                X = pilha[0]
                if tokens.size != 0:
                    a = tokens[0]
            else:
                print('Error')
                break
        else:
            topo = np.hstack([producoes[int(tabParsing[X][a])-1][:], pilha]) #empilha as producoes correspondentes
            if topo[0] == 1: # se topo vazio X recebe o novo topo da pilha
                X = topo[0] #
            else:
                if topo[0] != 0: # se topo nao vazio atualiza a pilha
                    pilha = np.delete(pilha,[0])
                    pilha = np.hstack([producoes[int(tabParsing[X][a])-1][:], pilha])
                    pilha = pilha[pilha != 0]
                    X = pilha[0]
                else:
                    print('Error')
                    break
print('Pilha: ')                
print(pilha)
print('Entrada: ')
print(tokens)
print('Sentença: ' + palavra +' reconhecida com sucesso')
        