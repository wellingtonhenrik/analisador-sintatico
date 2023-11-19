from parsing import TabParsing
import numpy as np

tokens = '' # Entrada

print(tokens)

erro = False
erroMsg = ''

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
    print("X: "+ str(X))
    print("a: " + str(a))
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
                erro = True
                erroMsg = 'Error, mismatch'
                break
        else:
            if int(tabelaParsing[X][a]) != 0: # se existe uma producao
                print('producao: '+str(tabelaParsing[X][a]))    
                pilha = np.delete(pilha,[0])
                pilha = np.hstack([producoes[int(tabelaParsing[X][a])][:], pilha]) #empilha as producoes correspondentes
                pilha = pilha[pilha != 0]  
                X = pilha[0]
            else:
                erro = True
                erroMsg = 'Error, no production'
                break

if erro:
    print(erroMsg)
else:
    print('Pilha: ')                
    print(pilha)
    print('Entrada: ')
    print(tokens)
    print('Sentença reconhecida com sucesso')