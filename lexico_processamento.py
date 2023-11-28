import numpy as np
from lexico_utils import *
from parsing import TabParsing

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
     # Variáveis para rastrear o escopo das variáveis
    variaveis_funcao = set()
    funcoes_tipos = {}

    def verificar_regras_semanticas(tokens):
        
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
        for i in range(len(lexemas) - 1):
            if lexemas[i] == 'var':
                variaveis_funcao.add(lexemas[i + 1])  

            if lexemas[i] == 'end':
                variaveis_funcao.clear() 

            if lexemas[i] == 'procedure':
                funcao = lexemas[i + 1]
                tipo_argumentos = []

                j = i + 3 
                while lexemas[j] != 'begin':
                    tipo_argumentos.append(lexemas[j])
                    j += 2

                funcoes_tipos[funcao] = tipo_argumentos  

            if lexemas[i] == 'ident' and lexemas[i - 1] == '(':
                funcao_chamada = lexemas[i]
                argumentos_chamada = []
                j = i + 1

                while lexemas[j] != ')':
                    argumentos_chamada.append(lexemas[j])
                    j += 2

                if funcao_chamada in funcoes_tipos:
                    tipos_esperados = funcoes_tipos[funcao_chamada]
                    if len(argumentos_chamada) != len(tipos_esperados):
                        print(f"Erro semântico: Número incorreto de argumentos para a função '{funcao_chamada}'.")
                        return False

                    for idx, arg in enumerate(argumentos_chamada):
                        if arg != tipos_esperados[idx]:
                            print(f"Erro semântico: Tipo incorreto para o argumento {idx + 1} da função '{funcao_chamada}'. Esperado: {tipos_esperados[idx]}, Recebido: {arg}.")
                            return False
                        
        return True


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

            if (lexema in lexemas_filtrados):
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
                    token = ''

                if token != '':
                    adicionar_token_e_lexema(tokens, lexemas, token, lexema, linha_numero, linha_atual)
                    lexema = ''

            i += 1
    
    if in_comment:
        print("Erro léxico: Comentário de bloco não foi fechado.")

    #exibir_tokens_e_lexemas(tokens, lexemas, linha_atual) # Apenas para entendimento, não é necessário para o funcionamento
    tokens = np.array(tokens)
    
    if verificar_regras_semanticas(lexemas):
        #tokenchumbado = [8,16,31,21,16,26,12,31,21,16,26,12,31,2,16,33,14,31,9,16,39,16,33,14,38,31,22,10,40,13,41,31,18,31,22,18,35] # Para testar com tokens especificos
        analise_sintatica(tokens)
    else:
        print("Falha na verificação das regras semânticas.")
    return tokens


def adicionar_token_e_lexema(tokens, lexemas, token, lexema, linha, linha_atual):
    tokens.append(token)
    lexemas.append(lexema)
    linha_atual.append(linha)

def exibir_tokens_e_lexemas(tokens, lexemas, linha_atual):
    for token, lexema, linha in zip(tokens, lexemas, linha_atual):
        print(f'Token: {token} - Lexema: {lexema} - Linha: {linha}')
    print(tokens) # [array de tokens] Apenas para entendimento, não é necessário para o funcionamento

def analise_sintatica(tokens):
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

        
