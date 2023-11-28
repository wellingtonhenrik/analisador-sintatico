from parsing import TabParsing
import numpy as np

def verificar_regras_semanticas(tokens, tokens_lexemas, lexemas):
    # Verificação de regras semânticas

    # Uma const nunca pode ser alterada
    if 'const' in tokens_lexemas.values():
        for i in range(len(tokens) - 1):
            if tokens[i] == 'const' and tokens[i + 1] == ':=':
                print("Erro semântico: Tentativa de modificar uma constante.")
                return False

    # String não pode ser utilizada em operações matemáticas
    if 'string' in tokens_lexemas.values():
        for i in range(len(lexemas) - 1):
            if lexemas[i] == 'string' and tokens[i + 1] in {'+', '-', '*', '/'}:
                print("Erro semântico: Uso de string em operação matemática não é permitido.")
                return False

    # Variável criada dentro da função não pode ser utilizada fora dela
    variaveis_funcao = set()
    for i in range(len(lexemas) - 1):
        if lexemas[i] == 'var':
            variaveis_funcao.add(lexemas[i + 1])

        if lexemas[i] == 'end':
            variaveis_funcao.clear()

        # Adapte a verificação para verificar se a variável está sendo utilizada fora da função aqui...

    # Função só poderá receber seu tipo
    # Implemente aqui a verificação dos parâmetros e do escopo da função...

    return True

tokens = '' # Entrada
tokens_lexemas = {}  # Mapeamento de tokens para seus lexemas
lexemas = []  # Lista de lexemas

print(tokens)

erro = False
erroMsg = ''

if verificar_regras_semanticas(tokens, tokens_lexemas, lexemas):
    
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

else:
    print("Falha na verificação das regras semânticas.")
