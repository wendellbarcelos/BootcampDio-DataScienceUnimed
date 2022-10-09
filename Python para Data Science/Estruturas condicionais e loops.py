#Exemplo de indentação - Usando um função para colocar o codigo indentado e ver o resultado e os erros

def sacar(valor):
    saldo = 500
    
    if valor <= saldo:
        print("Saque realizado")
        print('Retire seu dinheiro no caixa.\n')
    else:
        print('Saldo insuficiente!')
    
    print('Obrigado por ser nosso cliente!')
    

sacar(1000)


#Estruturas condicionais IF, ELIF, ELSE  -> Usando o exemplo do saque acima 

saldo = 1000
saque = int(input('Valor a sacar: '))

if saque <= saldo:
    print('Saldo realizado!')
else:
    print('Saldo insuficiente')
    
#Ex2 -> Estrutura condicional aninhada
opcao = int(input('Escolha uma opção: [1] Saque [2] Extrato: '))

if opcao == 1:
    saque = int(input('Valor a sacar: '))
    
    if saque <= saldo:
        print('Saldo realizado!')
    else:
        print('Saldo insuficiente')

elif opcao == 2:
    print('Imprimindo extrato!')
    print(f'Saldo: R$ {saldo:.2f}')
    
else:
    print('Valor invalido!')

#Ex. IF Ternario
saldo = 1000
saque = 500

status = 'Sucesso' if saque <= saldo else 'Falha'
print(f'{status} ao realizar o saque')


#ESTRUTURAS DE REPETIÇÃO - WHILE, FOR  -> Estruturas de loop
numero = input('Digite um número: ')
for indice in numero:
    print(indice)
    
#Ex2
texto = input('Digite um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
print()

#Ex3 Usando o for com a função built-in range
for n in range(10):
    print(n, end=' ')

#Ex4 -> Usando While e break
opcao = -1
while opcao != 0:
    opcao = int(input('Escolha uma opção: [0] Sair [1] Saque [2] Extrato: '))
    if opcao == 1:
        print('Saque realizado')
    elif opcao == 2:
        print('Imprimindo extrato')
    else:  # Diferente da opcao correta ele entra em outro if dentro do else
        if opcao == 0:
            print('Operação finalizada')
        else:
            print('Valor invalido')
            break  # Usando o break para parar o codigo caso a operação seja invalida

#Ex4 ->Usando While com contador
soma = 0
cont = 0
while cont != 5:
    n = int(input('Digite um numero: '))
    cont += 1
    soma += n
    
print('Total:',soma)

