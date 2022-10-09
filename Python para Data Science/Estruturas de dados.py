# ## Estrutura de dados - Lista
# Python inclui diversas estruturas de dados compostas, usadas para agrupar outros valores. A mais versátil é list (lista), que pode ser escrita como uma lista de valores (itens) separados por vírgula, entre colchetes. Os valores contidos na lista não precisam ser todos do mesmo tipo.

# Criando um lista - A liste é criada a partir de colchetes [] e atribuindo valores de tipos iguais ou diferente
lista = ['Uva', 'Maçã', 'Banana', 'Laranja']

# Imprimindo a lista
print(lista)

# Uma lista pode ser indexada ou fatiada, lembrando os indices em Python iniciam em 0, vejamos:
print(lista[2])  # Retorna o valor do indice 2
print(lista[1:3])  # Usando fatiamento (slice) para retornar os valores a partir do indice 1 ate o indice 3

# Lista de tipos - Na lista podemos colocar diversos tipos de dados de uma vez
lista2 = [1, 2, 3, 4, 4, 'Brasil', 'Japão', 6.585, 4.2, True, False]

print(lista2)
print(lista2[6])
print(lista2[0::2])  # Dessa forma o slice vai iniciar no 0 até o ultimo valor sendo seu passo de 2 em 2 

# Lista aninhadas ou matriz de lista - Vamos criar uma nova e usando as duas anteriores 
lista3 = [[5,4,8,'São Paulo'],['Rio de Janeiro', 'Minas Gerais']]
lista4 = [lista, lista2]  # Aqui usaremos as duas listas anteriores para criar, podendo usar quantas lista for necessario
lista5 = lista4 + lista3 + [78, 57, 522, 78.422]

print(lista3)  # Dessa forma teremos duas lista dentro de uma lista
print(lista4)
print(lista5)

# Dessa for o fatiamento se torna diferente pois cada lista passa a ser um indice e ter um indice dentro de cada uma

print(lista5[2])  # Retornará a lista no indice 2 vamos acessar os indices dentro dela
print(lista5[2][3])  # Assim acessamos os elementos dentro de lista de listas

# Diferentemente de strings, que são imutáveis, listas são mutáveis, sendo possível alterar elementos individuais de uma lista

lista2[2] = 'Bahia'  # Vamos alterar o valor do indice 2 
print(lista2)  # Sendo assim o valor que antes era 3 passou a ser Bahia

lista3[0][1] = 758  # Alterando em uma lista dentro de outra passa o indice da lista e o indice a mudar
print(lista3)

# Função Built-in len() - Devolve o comprimento (o número de itens) de um objeto. Sendo uma sequência como string, bytes, 
# tupla, lista, intervalo e coleção. 

# Podemos usar a função len para ter o tamanho da lista

print(len(lista5))  # A lista5 contém 4 listas e 4 objetos fora de lista.
print(len(lista4))

# Função built-in Range - Gera uma sequência de valores sendo eles inteiros, start -> stop -> step range(inicio, fim, passo)
# Para essa lista iremos usar outra função built-in a list(), ela gera uma lista a partir do range.

lista6 = list(range(1,100,8))  # Passamos o valor inicial, o valor final e o passo será de 8 e 8
print(lista6)  # O ultimo valor em python não é iteravel

# Metodo e funções Built-in iremos passar por todos os topicos
# Métodos Append, Clear, Count... 

# O método append() anexa um elemento ao final da lista.
lista6.append('Maracuja')
print(lista6)

# O método clear() remove todos os elementos de uma lista.
lista.clear()
print(lista)  # Retorna a lista vazia

# O método copy() retorna uma cópia da lista especificada.
x = lista2.copy()
print(x) # Retornará o valor da lista2

# O método count() retorna o número de elementos com o valor especificado.
print(lista2.count(4)) # Retornará a quantidade de vezes que o valor 4 aparece na lista

# O método extend() adiciona os elementos de lista especificados (ou qualquer iterável) ao final da lista atual.
lista5.extend(lista6)
print(lista5)

# O método index() retorna o indice (a posição) do valor especificado.
print(lista5.index(65))

# O método insert() insere o valor especificado na posição especificada.
lista.insert(0, 7887)
print(lista)

# O método pop() remove o elemento na posição especificada.
lista2.pop(8)
print(lista2)

# O método remove() remove a primeira ocorrência do elemento com o valor especificado.
lista6.remove('Maracuja')
print(lista6)

# O método reverse() inverte a ordem de classificação dos elementos.
lista6.reverse()
print(lista6)

# O método sort() classifica a lista em ordem crescente por padrão.
lista6.sort()
print(lista6)

# List Comprehension - Aplica uma expressão arbitrária ao invés de aplicar apenas uma função a uma sequência de elementos.
# LC nos permite a desenvolver listas usando uma notação diferente, seria uma linha de loop for, construida dentro de [].
# Normalmente usamos loops for quando trabalhamos com função Map() e usamos LC quando esta for mais fácil de ser aplicada, há
# vantagens substancial de desempenho ao utilizar a list Comprehension.

lista = [1, 2, 3, 4, 4, 6.585, 4.2, 84, 20]

# EX: lst = [x for x in sequência] --> Lista Comprehensions
x = [x for x in 'Python']  # Vamos criar exemplo simples.
print(x)

# Podemos usa-la de diversas forma sendo util em varios cenarios, retornando o valor elevado ao quadrado
y = [x ** 2 for x in lista]
print(y)

# Vamos retornar os valores pares de uma lista
pares = [x for x in lista if x % 2 == 0]
print(pares)

# Convertendo as temperaturas para Fahrenheit
temperatura = [0, 22.5, 40, 85, 100, 106]
tempe = [(temp * (9 / 5) + 32) for temp in temperatura]
print(tempe)

## Tuplas
# Uma tupla consiste em uma sequência de valores separados por vírgulas, vimos que listas e strings têm muitas propriedades em comum, como indexação e operações de fatiamento. Apesar de tuplas serem similares a listas, elas são frequentemente utilizadas em situações diferentes e com propósitos distintos. Tuplas são imutáveis, e usualmente contém uma sequência heterogênea de elementos que são acessados via desempacotamento ou índice. Listas são mutáveis, e seus elementos geralmente são homogêneos e são acessados iterando sobre a lista.

# A criação de uma tupla é simples como a lista ela é representada por ()
tupla = ()
print(tupla)  # Uma tupla vazia

# Vamos atribuir valores a ela - assim como lista ela aceita todos os tipos de dados
tupla = ('Maria', 8445, 8.3, True)
print(tupla)

# A diferença da tupla para a lista é que tuplas são imutaveis seus valores não mudam
# ela nao aceita append, del item, adicionar ou mudar o valor do item.

#del tupla[0]  # Retorna um error informando que tupla não suporta deletação de itens
#tupla.append(85)  # Assim como no del acontece no append

# Podemos usar o len para retonar o tamanho da tupla e o index a partir de um valor
len(tupla)
print(tupla.index(8.3))  # Assim retorna o indice do valor

# Podemos deletar a tupla inteira usando o 'del tupla'

# Alterando um elemento através da função list
tupla = list(tupla)
print(tupla)  # Dessa forma alteramos a tupla em lista 

tupla.append('Marcus')  # Adicionamos um valor no final da lista 

tupla = tuple(tupla)  # Alteramos novamente para tupla apos adicionar o novo valor
print(tupla)


## Estrutura de dados - Conjuntos
# Sets (ou, como iremos chamar daqui para a frente, conjuntos) são estruturas disponíveis como builtins do Python, utilizadas para representar coleções desordenadas de elementos únicos. É importante sempre lembrar dos conjuntos por suas duas principais características:

# 1- Os elementos não são armazenados em uma ordem específica e confiável;
# 2- Conjuntos não contém elementos repetidos.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))

#Essa operação é muito útil quando precisamos descobrir elementos que duas listas possuem em comum:
l1 = [1, 2, 3]
l2 = [2, 4, 3]
print(set(l1).intersection(l2))

#A diferença entre dois conjuntos A e B retorna somente os elementos de A que não estão em B, ou seja, retira de A todos os elementos comuns a ambos os conjuntos:
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.difference(b))
print(b.difference(a))

## Estrutura de dados - Dicionários
# O dicionário, cujo tipo é dict () são também chamados de “memória associativa” ou “vetor associativo” em outras linguagens. Diferente de sequências que são indexadas por inteiros, dicionários são indexados por chaves (keys), que podem ser de qualquer tipo imutável (como strings e inteiros).

# A forma mais simples de criar um dicionário é usando as chaves {}
dic = {}
print(dic)  # Retornará um dicionário vazio 

# Vamos entender o conceito do dicionário, ele é uma estrutura de mapeamento muito utilizado para armazenar dados categoricos
# como em bancos de dados você tem a chave e o valor atribuido, como em um sistema de cadastro Key: value vejamos:

dic = {'Maria': 24, 'João': 18, 'Lucas': 33, 'Pedro': 47}  # Aqui temos os nomes sendo as chaves e a idade recebendo os valores
print(dic)

# Podemos retornar a partir de suas chaves ex:
print(dic['João'])  # O retorno será idade de joão

# Podemos inserir valores 
dic['Marcus'] = 62
print(dic)  # No fim ele reconhece que não existe Marcus e adiciona o valor

# Alterar um valor é simples ele retorna a chave e altera o valor
dic['Pedro'] = 48
print(dic) 

# Deletar valores a partir da chave usando a função del
del dic['Marcus']
print(dic)  # Podemos usar a função em qualquer chave

# Retornando uma lista de chaves
print(list(dic))  # dessa forma retornará todos as chaves em uma lista

# E usar o sorted para ordernar as chaves
print(sorted(dic))

# Usando o metódo clear para limpar o dicionário e o del para apagar
dic.clear()
print(dic)  # Ele retornará o valor vazio do dicionário
del dic # Apagará o dicionario
# dic Ele rotorna um erro informando que não existe mais o dicionário

# Criando um novo dicionário
nomes = {'Maria': 24, 'João': 18, 'Lucas': 33, 'Pedro': 47}
print(nomes)

# Usando a função len podemos retornar o tamanho do dicionário
print(len(nomes))

# E usando as funções keys e values ele vai nos retornar as chaves e os valores
print(nomes.keys())
print(nomes.values())

# A função items retorna cada item do dicionario com o seu valor
print(nomes.items())

# Vamos criar outro dicionário para usar a função upgrade
nomes2 = {'Roger': 34, 'Marta': 23}
nomes.update(nomes2)  # Usando o upgrade
print(nomes)  # Teremos uma concatenação dos valores

# Criando uma lista de dicionário
cadastro = [{
    'id': 1,'nome': 'Claudio','idade': 43,'sexo': 'M'},
    {'id': 2,'nome': 'Vitor','idade': 19,'sexo': 'M'}]

print(cadastro) 
print(cadastro[0])  # Podemos retornar apenas os valores do dicionário no indice 0

# Criando um dicionário de listas
dic2 = {'key1': 8554, 'key2': [54,8441,23,471], 'key3': ['Maçã', 'Uva']}
print(dic2)
print(dic2['key2'][1]) # Da mesma forma podemos usar os indices para retonar valores
print(dic2['key3'][1].upper())  # Podemos usar funções a partir dos indices

# Dicionario aninhado

dicio3 = {
    'id_1': {'nome': 'Claudio','idade': 43,'sexo': 'M'},
    'id_2': {'nome': 'Vitor','idade': 19,'sexo': 'M'},
    'id_3': {'nome': 'Maria','idade': 29,'sexo': 'F'}
}

print(dicio3)

# Usando o for e a função Items(), ambos retornam da msm forma
# Usando o for para retornar
for valor in dicio3:
    print(valor, dicio3[valor])

# Usando a função items
for chave, valor in dicio3.items():
    print(chave, valor)

# Metodos do dicionario
#dict.clear() - Ele limpa o dicionario da mesma forma de lista
#dict.copy() - Ele faz uma copia do dicionario
#dict.fromkeys() - Ele criar chaves sem nenhum valor ou com valores unicos
    # dict.fromkeys(['nome', 'telefone']) -> {'nome': None, 'telefone': None}
    # dict.fromkeys(['nome', 'telefone'], 'vazio') -> {'nome': vazio, 'telefone': vazio}
#dict.get() - Ele acessa os valores, usado quando não sabemos se o valor existe
#dict.items() - Retorna os itens do dicionario
#dict.keys() - Retorna somente as chaves do dicionario
#dict.values() - Retorna somente os valores do dicionario
#dict.pop() - Remove uma chave do dicionario
#dict.setdefault() - Ele busca as chaves e verifica se existe caso nao existe ele cria com o valor.
#dict.update() - Ele permite atualizar o dicionario com outro dicionario, caso a chave ja exista ele atualiza a chave existente.
#in - Ele verifica se um valor esta dentro do dicionario
    # resultado = 'maria helena' in dados 
    # print(resultado) -> True
    # resultado = 'idade' in contatos['id_1']
    # print(resultado) -> False
#del - Deleta um elemento do dicionario ou todos os elementos
    # del contatos['id_1']['telefone] -> delete apenas o elemento informado
    # del contatos['id_1'] -> deleta todos os elementos da chave

