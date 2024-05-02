palavra = "|Bem vindo a loja do Allan Crissanto|" 
print("-"*len(palavra)) #Visual de boas vindas
print(palavra) #Print de boas vindas
print("-"*len(palavra)) 

valor = int(input("Digite o valor do produto: ")) 
quantidade = int(input("Digite a quantidade do produto: ")) 
valorTotal = valor * quantidade #Calculo do valor total

#Condição para o desconto
if valorTotal < 2500: #Se o valor for menor que 2500, o desconto é 0%
    desconto = 0
elif valorTotal >= 2500 and valorTotal < 6000: #Se o valor for maior ou igual a 2500 e menor que 6000, o desconto é 4%
    desconto = 4
elif valorTotal >= 6000 and valorTotal < 10000:#Se o valor for maior ou igual a 6000 e menor que 10000, o desconto é 7%
    desconto = 7
else: #Se o valor for maior ou igual a 10000, o desconto é 11%
    desconto = 11

ValorDesconto = (valorTotal * (desconto / 100)) #Calculo do desconto
ValorTotalComDesconto = valorTotal - ValorDesconto #Calculo do valor total com desconto

print(f"O valor total sem desconto é: R${valorTotal:.2f}") #Print do valor total sem desconto
print(f'O valor total com desconto é: {ValorTotalComDesconto:.2f}')#Print do valor total com desconto
