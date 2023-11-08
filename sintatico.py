import numpy as np
from parsing import TabParsing

# Tokens virão do analisador léxico
tokens = [8, 16, 31, 2, 16, 33, 14, 31, 22, 18, 35]

print(tokens) 
tokens = np.array(tokens)

# Inicializar a Matriz de Parsing com zeros.
tabParsing = TabParsing()
tabParsing.inicializarTab()
tabParsing.inicializarProdu()

# Tabela de parsing populada
tabelaParsing = tabParsing.tabParsing

# Tabela de produções populada
producoes = tabParsing.producoes

pilha = [43] #$ topo da pilha - gramatica

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
        if X <= 44: #topo da pilha é um terminal
            if X == a: #deu match
                pilha = np.delete(pilha,[0])
                tokens = np.delete(tokens,[0])
                X = pilha[0]
                if tokens.size != 0:
                    a = tokens[0]
            else:
                print('Error')
                break
        else:
            topo = np.hstack([producoes[int(tabelaParsing[X][a])][:], pilha]) #empilha as producoes correspondentes
            if topo[0] == 44: # se topo vazio X recebe o novo topo da pilha
                X = topo[0] #
            else:
                if topo[0] != 44: # se topo nao vazio atualiza a pilha
                    pilha = np.delete(pilha,[0])
                    pilha = np.hstack([producoes[int(tabelaParsing[X][a])][:], pilha])
                    pilha = pilha[pilha != 0]
                    X = pilha[0]
                else:
                    print('Error')
                    break
print('Pilha: ')                
print(pilha)
print('Entrada: ')
print(tokens)
print('Sentença reconhecida com sucesso')
        