# FUNÇÃO - é um conjunto de codigo que você usa mais de uma vez passando apenas os parametros e chamando a função
# Definindo uma função
def funcao(): # Usando a palavra reservada def nome da função (parametros):
    print('Hello World') # O retorno da função onde vem todos os codigos
    
funcao() # Chamando a função e passando os dados de parametro


# Definindo função com parametro
def funcao_ola(nome): # Passamos um parametro para a função na qual ele irá receber o dado de entrada
    print(f'Olá {nome}, tudo bem?') # Iremos retornar uma string usando o parametro
    
funcao_ola('Wendell') # passamos o parametro


# Podemos usar função de diversas formas e todos os dados de entrada
# Usando lista

def calculadora(lista, n): # Definimos a função com dois parametros
    lst = []  # Criamos uma lista vazia para receber os valores
    for i in lista: # Usamos um loop for para pegar todos os valores
        lst.append(i * n)  # Cada indice da lista sera multiplicado e adicionado a lista vazia
    return lst  # Retornaremos a lista com os valores

lista = list(range(1,10))  # Criamos uma lista
calculadora(lista, 2)  # Chamamos a função e passamos os parametros


# Vamos fazer uma divisão de texto usando a função split 
def split_string(texto):  # Criamos a função com um parametro
    return texto.split(' ')  # Retornamos o texto passando pela função split


texto = 'Eu faço da dificuldade a minha motivação. A volta por cima vem na continuação.'
print(split_string(texto.upper()))  # Usando a função Upper

# Quando não temos a quantidade de parametros para a função usamos o arg
def printVarInfo(param, *params):
    # Imprimindo o valor do primeiro argumento
    print(f'O parâmetro passado foi: {param}')
    
    # Imprimindo o valor do segundo argumento
    for item in params:
        print(f'O parâmetro passado foi: {item}')
    return;

printVarInfo(10)
printVarInfo('Laranja', 'Maçã', 'Abacaxi')  # Passando varios parametros 


# Objetos de primeira classe
# Temos uma função que gera todo o resultado, mas criamos outras que funções que usam dela

def somar(a, b):  # Criamos a primeira função que retorna uma soma
    return a + b

def subtrair(a, b):  # Criamos a primeira função que retorna uma soma
    return a - b

def multiplicar(a, b):  # Criamos a primeira função que retorna uma soma
    return a * b

def exibir_resultado(a, b, funcao):  #Ela sozinha não retorna nada
    resultado = funcao(a, b)
    print(f'O resultado da operação é = {resultado}')

#print(exibir_resultado(10, 10) ) # Somente ela não retorna nada sim erro
exibir_resultado(10, 10, somar)  # Passando o argumento e a função que fará a operação
exibir_resultado(10, 10, subtrair)
exibir_resultado(10, 10, multiplicar)
