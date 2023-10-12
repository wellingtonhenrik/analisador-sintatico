import numpy as np
from lexico_utils import *

def le_arquivo(caminho):
    # Lê o arquivo e garante que será fechado automaticamente
    with open(caminho, "r") as arquivo:
        return processar_arquivo(arquivo)

def processar_arquivo(arquivo):
    # Dicionário para armazenar os tokens e lexemas
    tokens_lexemas = {
        1: "while",
        2: "var",
        3: "to",
        4: "then",
        5: "string",
        6: "real",
        7: "read",
        8: "program",
        9: "procedure",
        10: "print",
        11: "nreal",
        12: "nint",
        13: "literal",
        14: "integer",
        15: "if",
        16: "ident",
        17: "for",
        18: "end",
        19: "else",
        20: "do",
        21: "const",
        22: "begin",
        23: "vstring",
        24: ">=",
        25: ">",
        26: "=",
        27: "<>",
        28: "<=",
        29: "<",
        30: "+",
        31: ";",
        32: ":=",
        33: ":",
        34: "/",
        35: ".",
        36: ",",
        37: "*",
        38: ")",
        39: "(",
        40: "{",
        41: "}",
        42: "-"
    }

    valores_a_excluir = {"nreal", "nint", "literal", "ident", "vstring"}

    tokens_lexemas_filtrado = {chave: valor for chave, valor in tokens_lexemas.items() if valor not in valores_a_excluir}
    
    lexemas_array = list(tokens_lexemas.values())
    lexemas_filtrados = list(tokens_lexemas_filtrado.values())

    tokens = []
    lexemas = []
    linha_atual = []
    in_comment = False

    for linha_numero, linha in enumerate(arquivo, start=1):
        lexema = ''
        i = 0

        while i < len(linha):
            if in_comment:
                # Dentro do comentário de bloco, ingora os caracteres até encontrar a sequencia '*/'
                if linha[i:i+2] == '*/':
                    in_comment = False
                    i += 2
                else:
                    i += 1
                continue

            if linha[i:i+2] == '//':
                # Comentário de linha, ignora o restante da linha
                break

            if linha[i:i+2] == '/*':
                # Inicio do comentário de bloco
                in_comment = True
                i += 2
                continue

            if linha[i] in lexemas_filtrados: 
                if lexema.strip() != '':
                    # Identificador
                    validar_identificador(linha_numero, lexema)
                    token = lexemas_array.index('ident') + 1
                    adicionar_token_e_lexema(tokens, lexemas, token, lexema, linha_numero, linha_atual)
                lexema = linha[i]
            elif linha[i] != ' ' or lexema.startswith("'"):
                lexema = lexema + linha[i]
            else:
                if lexema.strip() != '':
                    # Identificador
                    validar_identificador(linha_numero, lexema)
                    token = lexemas_array.index('ident') + 1
                    adicionar_token_e_lexema(tokens, lexemas, token, lexema, linha_numero, linha_atual)
                    lexema = ''

            if lexema in lexemas_filtrados:
                # Verifica se o próximo caractere forma um operador composto. Casos do tipo <> :=
                if i + 1 < len(linha) and lexema + linha[i + 1] in lexemas_filtrados: 
                    lexema += linha[i + 1]
                    token = lexemas_array.index(lexema) + 1
                    i += 2
                    adicionar_token_e_lexema(tokens, lexemas, token, lexema, linha_numero, linha_atual)
                    lexema = ''
                    continue

                token = lexemas_array.index(lexema) + 1
                adicionar_token_e_lexema(tokens, lexemas, token, lexema, linha_numero, linha_atual)
                lexema = ''
            else:
                # Verifica se é uma string
                if verificar_string(lexema):
                    validar_string(linha_numero, lexema)
                    token = lexemas_array.index('vstring') + 1
                # Verifica se é um número
                elif verificar_numero_inteiro(lexema):
                    while i + 1 < len(linha) and verificar_numero_inteiro(linha[i + 1]):
                        lexema += linha[i + 1]
                        i += 1
                    # Verifica se é real
                    if linha[i + 1] == '.':
                        lexema += linha[i + 1]
                        i += 1
                        while i + 1 < len(linha) and verificar_numero_inteiro(linha[i + 1]):
                            lexema += linha[i + 1]
                            i += 1
                        if verificar_numero_real(lexema):
                            validar_numero_real(linha_numero, lexema)
                            token = lexemas_array.index('nreal') + 1
                    else:          
                        validar_numero_inteiro(linha_numero, lexema)
                        token = lexemas_array.index('nint') + 1
                # Verifica se é um literal
                elif lexema == '"':
                    while i + 1 < len(linha):
                        lexema += linha[i + 1]
                        i += 1
                        if linha[i] == '"' and not lexema == '"':
                            break
                    validar_literal(linha_numero, lexema)
                    token = lexemas_array.index('literal') + 1
                else:
                    # if lexema:
                    #     token = lexemas_array.index('ident') + 1
                    #     adicionar_token_e_lexema(tokens, lexemas, token, lexema, linha_numero, linha_atual)
                    #     lexema = ''
                    # else:
                    token = ''

                if token != '':
                    adicionar_token_e_lexema(tokens, lexemas, token, lexema, linha_numero, linha_atual)
                    lexema = ''

            i += 1
    
    if in_comment:
        print("Erro léxico: Comentário de bloco não foi fechado.")

    #exibir_tokens_e_lexemas(tokens, lexemas, linha_atual) # Apenas para entendimento, não é necessário para o funcionamento
    tokens = np.array(tokens)
    #return tokens

def adicionar_token_e_lexema(tokens, lexemas, token, lexema, linha, linha_atual):
    tokens.append(token)
    lexemas.append(lexema)
    linha_atual.append(linha)

def exibir_tokens_e_lexemas(tokens, lexemas, linha_atual):
    for token, lexema, linha in zip(tokens, lexemas, linha_atual):
        print(f'Token: {token} - Lexema: {lexema} - Linha: {linha}')
    print(tokens) # [array de tokens] Apenas para entendimento, não é necessário para o funcionamento
        
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

pilha = np.hstack([producoes[0][:], pilha]) # Verificar o que isso realmente faz, com exemplos

print(pilha)

X = pilha[0]
a = tokens[0]

while X != 5: #enquanto pilha nao estiver vazia (trocar pelo numero do $ da gramatica)
    print(X)
    print(a)
    print(pilha)
    if X == 1: #se o topo da pilha for vazio (verificar numero do vazio da gramatica p mudar)
        pilha = np.delete(pilha,[0])
        X = pilha[0]
    else:
        if X <= 5: #topo da pilha eh um terminal ($?)
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
            if topo[0] == 1: # se topo vazio X recebe o novo topo da pilha (verificar numero do vazio da gramatica p mudar)
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
