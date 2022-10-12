### Programação orientada a objetos (POO)
# Um paradigma de programação é um estilo e programação. Não é uma linguagem (Python, Java, C, etc), e sim a forma como você soluciona os problemas através do código.

# O paradigma de programação orientada a objetos estrutura o código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais modular e extensível. Os dois conceitos chaves para aprender POO são: classes e objetos.

## Classes e Objetos?
# Uma classe define as características e comportamentos de um objeto, porém não conseguimos usá-las diretamente. Já os objetos podemos usá-los e eles possuem as características e comportamentos que foram definidos nas classes.

class Cachorro:  # Chamando a classe
    def __init__(self, nome, cor, acordado=True):  #  Inicinando 
        self.nome = nome  # Atributo = Caracteristica da classe
        self.cor = cor  # Atributo = Caracteristica da classe
        self.acordado = acordado  # Atributo = Caracteristica da classe

    def latir(self):  # Método = Comportamento
        print("Auau")

    def dormir(self):  # Método = Comportamento
        self.acordado = False
        print("Zzzzz...")

# Criamos a classe agora precisamos chamar os objetos
cao_1 = Cachorro("chappie", "amarelo", False)  # Passando as caracteristicas da classe
cao_2 = Cachorro("Aladim", "branco e preto")  # Passando as caracteristicas da classe
cao_1.latir()  # Chamando o comportamento da classe
print(cao_2.acordado)  # Imprimindo o comportamento: retorno True
cao_2.dormir()  # Chamando o comportamento da classe
print(cao_2.acordado)  # Imprimindo o comportamento: retorno False

#########################################

# Exemplo pratico: João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!

class Bicicletaria:
    def __init__(self, cor, modelo, ano, valor):  # Paramentros
        self.cor = cor  # Atributo = Caracteristicas
        self.modelo = modelo  # Atributo = Caracteristicas
        self.ano = ano  # Atributo = Caracteristicas
        self.valor = valor  # Atributo = Caracteristicas
    
    def buzinar(self):  # Metodo = Comportamentos
        print('Biih bi...')
        
    def parar(self):  # Metodo = Comportamentos
        print('Parando bicicleta...')
        print('Bicicleta parada...')
        
    def correr(self):  # Metodo = Comportamentos
        print('Vrun vrun...')
        
    # Para retornar a classe com todas as caracteristicas usamos o metodo __str__
    # def __str__(self):
    #     return f'Bicicleta: {self.modelo}, {self.cor}, {self.ano}, {self.valor}'
    
    # Deixando o codigo mais automatizado -> melhor forma de uso
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

# Chamando os objetos
bicicleta1 = Bicicletaria('Preta', 'Poty', 2012, 699.00)
bicicleta2 = Bicicletaria('Vermelha', 'Caloi', 2009, 497.00)
bicicleta3 = Bicicletaria('Rosa', 'Cecci', 2002, 369.00)

# Retornando as caracteristicas 
print(bicicleta1.valor)  # Retornando o valor da bicicleta 1
bicicleta1.buzinar()  # Retornando comportamento da bicicleta 1

print(bicicleta2.modelo)  # Retornando o valor da bicicleta 2
bicicleta2.correr()
bicicleta2.parar()  # Retornando comportamento da bicicleta 2

print(bicicleta1)  # Retornando todas as caracteristicas da classe
print(bicicleta2)
print(bicicleta3)

#########################################

### Método Construtor e Método Desconstrutor
# O método construtor sempre é executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nosso objeto. Para declarar o método construtor da classe, criamos um método com o nome __init__.

# O método destrutor sempre é executado quando uma instância (objeto) é destruída. Destrutores em Python não são tão necessários quanto em C++ porque o Pyton tem um coletor de lixo que lida com o gerenciamento de memória automaticamente. Para declarar o método destrutor da classe, criamos um método com o nome __del__
class Cachorro:
    def __init__(self, nome, cor, acordado=True):  # O __init__ é o metodo de inicialização (construtor) da classe
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print('Au au...')

    # Método desconstrutor - No final da operação ele exclui o objeto 
    def __del__(self):  # O __del__ é o metodo desconstrutor da classe
        print("Destruindo a instância")

c = Cachorro('bob', 'caramelo', False)
c.latir()
del c # dessa forma iremos forçar o metodo a excluir o objeto e pode ser usado em varias partes do codigo


## Herança
# Em programação herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai (base).

# Beneficios da herança
# ● Representa bem os relacionamentos do mundo real.
# ● Fornece reutilização de código, não precisamos escrever o mesmo código repetidamente. Além disso, permite adicionar mais recursos a uma classe sem modificá-la.
# ● É de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A.

#Ex
class Pai():
    pass

class Filho(Pai):
    pass

##########################################

### Herança Simples 
# Quando uma classe filha herda apenas uma classe pai, ela é chamada de herança simples.

class Veiculo:
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas
        
    def ligar_motor(self):
        print('Ligando o motor...')
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"
    
        
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas, carregado):
        super().__init__(cor, placa, num_rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} esta carregado")


moto = Motocicleta('Azul', 'HUD-8445', 2)
carro = Carro('Verde', 'LKI-5421', 4)
caminhao = Caminhao('Azul', 'PPD-6566', 8, True)

# Chamando outra classe instanciada
caminhao.esta_carregado()
print(moto)
print(carro)
print(caminhao)


#########################################
### Herança Multipla - Muito cuidado para usar essa forma
# Quando uma classe filha herda de várias classes pai, ela é chamada de herança múltipla.

class Animal:
    def __init__(self, n_patas):
        self.n_patas = n_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"
    
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Gato(Mamifero):
    pass

class Onitorrinco(Mamifero, Ave):
    pass


gato = Gato(n_patas=4, cor_pelo='Branco')
onitorrinco = Onitorrinco(n_patas=2, cor_pelo='Marron', cor_bico='Amarelo')

print(gato)
print(onitorrinco)

#########################################

### Encapsulamento
# O encapsulamento é um dos conceitos fundamentais em programação orientada a objetos. Ele descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma unidade. Isso impõe restrições ao acesso direto a variáveis e métodos e pode evitar a modificação acidental de dados. Para evitar alterações acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto.

# Em linguagens como Java e C++, existem palavras reservadas para definir o nível de acesso aos atributos e métodos da classe. Em Python não temos palavras reservadas, porém usamos convenções no nome do recurso, para definir se a variável é pública ou privada.

# ● Público: Pode ser acessado de fora da classe.
# ● Privado: Só pode ser acessado pela classe

## Público e Privado
# Todos os recursos são públicos, a menos que o nome inicie com underline. Ou seja, o interpretador Python não irá garantir a proteção do recurso, mas por ser uma convenção amplamente adotada na comunidade, quando encontramos uma variável e/ou método com nome iniciado por underline, sabemos que não deveríamos manipular o seu valor diretamente, ou invocar o método fora do escopo da classe.


class Conta:
    def __init__(self, num_agencia, saldo=0):
        self.num_agencia = num_agencia
        self._saldo = saldo
        
    def depositar(self,valor):
        # ... Implementar codigo
        self._saldo += valor
    
    def sacar(self,valor):
        # ... Implementar codigo
        self._saldo -= valor
    
    # Criando um método para retonar a variavel privada    
    def extrato(self):
        self.agencia = input('Digite agencia: ')
        if self.num_agencia == self.agencia:
            return f"Saldo: {self._saldo}"
        else:
            return 'Agencia invalida'

conta = Conta('851420', 100)
conta.depositar(200)  # Usando métodos para deposito
print(conta.extrato())  # Usando um método para retorno da variavel privada.

# print(conta._saldo) # Jamais manipule uma variavel privada dessa forma, por convenção se tem o undeline não deve ser manipulada fora do escopo da classe, pois é uma variavel privada.

#########################################

## Property()
# Com o property() do Python, você pode criar atributos gerenciados em suas classes. Você pode usar atributos gerenciados, também conhecidos como propriedades, quando precisar modificar sua implementação interna sem alterar a API pública da classe.

class Foo:
    def __init__(self, x=None): # O valor do atributo inicia 0
        self._x = x
        
    @property # Obtendo o valor do atributo privado
    def x(self):
        return self._x or 0
    
    @x.setter  # Mudando o valor do atributo privado
    def x(self, value):
        self._x += value
        
    @x.deleter  # Deletando o valor do atributo privado
    def x(self):
        self._x = 0

foo = Foo(10) # Adicionando o valor do objeto
print(foo.x) # Retorno 25
foo.x = 15 # Vamos modificar o objeto adicionando mais 15
print(foo.x) # Retorno 25
del foo.x # Deletando o valor, zerando o valor
print(foo.x) # retorno 0

# Ex2
class Pessoa:
    def __init__(self, nome, ano_nasc):
        self.nome = nome
        self._ano_nasc = ano_nasc
        
    # Não tendo nenhuma logica para criar uma property usando atributo privado, não faz sentido criar, usa o atributo publico que faz mais sendido
    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nasc
    
pessoa = Pessoa('Wendell', 1991)
print(f'Nome: {pessoa.nome} | idade: {pessoa.idade}')
#########################################

### Polimorfismo
## A palavra polimorfismo significa ter muitas formas. Na programação, polimorfismo significa o mesmo nome de função (mas assinaturas diferentes) sendo usado para tipos diferentes.

## Na herança, a classe filha herda os métodos da classe pai. No entanto, é possível modificar um método em uma classe filha herdada da classe pai. Isso é particularmente útil nos casos em que o método herdado da classe pai não se encaixa perfeitamente na classe filha.

## Conceito 
class Passaro:
    def voar(self):
        print('Voando...')
class Pardal(Passaro):
    def voar(self):
        print('Pardal pode voar')
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

class Aviao(Passaro): # Uso apenas como exemplo totalmente errado o uso
    def voar(self):
        print("Avião está decolando")

def plano_de_voo(obj): # O conceito está aqui
    obj.voar() # O objeto precisa receber o metodo voar

plano_de_voo(Pardal())  # Passando a instancia do metodo para o objeto
plano_de_voo(Avestruz()) # Passando a instancia do metodo para o objeto
plano_de_voo(Aviao())

### Variáveis de classe e variáveis de instância
## Todos os objetos nascem com o mesmo número de atributos de classe e de instância. Atributos de instância são diferentes para cada objeto (cada objeto tem uma cópia), já os atributos de classe são compartilhados entre os objetos.

##########################################
class Estudante:
    escola = "DIO"  # Variavel de classe
    
    def __init__(self, nome, matricula):
        self.nome = nome  # Variavel de instancia
        self.matricula = matricula  # Variavel de instancia
        
    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
aluno1 = Estudante("Guilherme", 56451)
aluno2 = Estudante("Giovanna", 17323)
mostrar_valores(aluno1, aluno2)

Estudante.escola = 'Python'  # Mudando o valor da variavel de classe
aluno3 = Estudante('Marcus', 35774)
mostrar_valores(aluno1, aluno2, aluno3)

#########################################

### Método de Classe e Método Estático
## Métodos de classe estão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a instância do objeto

## Um método estático não recebe um primeiro argumento explícito. Ele também é um método vinculado à classe e não ao objeto da classe. Este método não pode acessar ou modificar o estado da classe. Ele está presente em uma classe porque faz sentido que o método esteja presente na classe.

## ● Um método de classe recebe um primeiro parâmetro que aponta para a classe, enquanto um método estático não.
## ● Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessálo ou modificá-lo.
## ● Geralmente usamos o método de classe para criar métodos de fábrica.
## ● Geralmente usamos métodos estáticos para criar funções utilitárias.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @classmethod
    def criar_de_data_nasc(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
# p = Pessoa('Joao', 32)
# print(p.nome, p.idade)

p = Pessoa.criar_de_data_nasc(1991, 11, 30, 'Wendell')
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))

##########################################

