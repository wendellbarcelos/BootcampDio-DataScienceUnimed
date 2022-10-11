# ### Programação orientada a objetos (POO)
# # Um paradigma de programação é um estilo e programação. Não é uma linguagem (Python, Java, C, etc), e sim a forma como você soluciona os problemas através do código.

# # O paradigma de programação orientada a objetos estrutura o código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais modular e extensível. Os dois conceitos chaves para aprender POO são: classes e objetos.

# ## Classes e Objetos?
# # Uma classe define as características e comportamentos de um objeto, porém não conseguimos usá-las diretamente. Já os objetos podemos usá-los e eles possuem as características e comportamentos que foram definidos nas classes.

# class Cachorro:  # Chamando a classe
#     def __init__(self, nome, cor, acordado=True):  #  Inicinando 
#         self.nome = nome  # Atributo = Caracteristica da classe
#         self.cor = cor  # Atributo = Caracteristica da classe
#         self.acordado = acordado  # Atributo = Caracteristica da classe

#     def latir(self):  # Método = Comportamento
#         print("Auau")

#     def dormir(self):  # Método = Comportamento
#         self.acordado = False
#         print("Zzzzz...")

# # Criamos a classe agora precisamos chamar os objetos
# cao_1 = Cachorro("chappie", "amarelo", False)  # Passando as caracteristicas da classe
# cao_2 = Cachorro("Aladim", "branco e preto")  # Passando as caracteristicas da classe
# cao_1.latir()  # Chamando o comportamento da classe
# print(cao_2.acordado)  # Imprimindo o comportamento: retorno True
# cao_2.dormir()  # Chamando o comportamento da classe
# print(cao_2.acordado)  # Imprimindo o comportamento: retorno False

# # Exemplo pratico: João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!

# class Bicicletaria:
#     def __init__(self, cor, modelo, ano, valor):  # Paramentros
#         self.cor = cor  # Atributo = Caracteristicas
#         self.modelo = modelo  # Atributo = Caracteristicas
#         self.ano = ano  # Atributo = Caracteristicas
#         self.valor = valor  # Atributo = Caracteristicas
    
#     def buzinar(self):  # Metodo = Comportamentos
#         print('Biih bi...')
        
#     def parar(self):  # Metodo = Comportamentos
#         print('Parando bicicleta...')
#         print('Bicicleta parada...')
        
#     def correr(self):  # Metodo = Comportamentos
#         print('Vrun vrun...')
        
#     # Para retornar a classe com todas as caracteristicas usamos o metodo __str__
#     # def __str__(self):
#     #     return f'Bicicleta: {self.modelo}, {self.cor}, {self.ano}, {self.valor}'
    
#     # Deixando o codigo mais automatizado -> melhor forma de uso
#     def __str__(self):
#         return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

# # Chamando os objetos
# bicicleta1 = Bicicletaria('Preta', 'Poty', 2012, 699.00)
# bicicleta2 = Bicicletaria('Vermelha', 'Caloi', 2009, 497.00)
# bicicleta3 = Bicicletaria('Rosa', 'Cecci', 2002, 369.00)

# # Retornando as caracteristicas 
# print(bicicleta1.valor)  # Retornando o valor da bicicleta 1
# bicicleta1.buzinar()  # Retornando comportamento da bicicleta 1

# print(bicicleta2.modelo)  # Retornando o valor da bicicleta 2
# bicicleta2.correr()
# bicicleta2.parar()  # Retornando comportamento da bicicleta 2

# print(bicicleta1)  # Retornando todas as caracteristicas da classe
# print(bicicleta2)
# print(bicicleta3)


# ### Método Construtor e Método Desconstrutor
# # O método construtor sempre é executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nosso objeto. Para declarar o método construtor da classe, criamos um método com o nome __init__.

# # O método destrutor sempre é executado quando uma instância (objeto) é destruída. Destrutores em Python não são tão necessários quanto em C++ porque o Pyton tem um coletor de lixo que lida com o gerenciamento de memória automaticamente. Para declarar o método destrutor da classe, criamos um método com o nome __del__
# class Cachorro:
#     def __init__(self, nome, cor, acordado=True):  # O __init__ é o metodo de inicialização (construtor) da classe
#         self.nome = nome
#         self.cor = cor
#         self.acordado = acordado
    
#     def latir(self):
#         print('Au au...')

#     # Método desconstrutor - No final da operação ele exclui o objeto 
#     def __del__(self):  # O __del__ é o metodo desconstrutor da classe
#         print("Destruindo a instância")

# c = Cachorro('bob', 'caramelo', False)
# c.latir()
# del c # dessa forma iremos forçar o metodo a excluir o objeto e pode ser usado em varias partes do codigo


### Herança
# Em programação herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai (base).

## Beneficios da herança
# ● Representa bem os relacionamentos do mundo real.
# ● Fornece reutilização de código, não precisamos escrever o mesmo código repetidamente. Além disso, permite adicionar mais recursos a uma classe sem modificá-la.
# ● É de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A.

#Ex
class Pai():
    pass

class Filho(Pai):
    pass

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
