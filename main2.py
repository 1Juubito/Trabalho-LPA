palavra = "|Bem vindo a loja de Gelados do Allan Crissanto|"
print("-"*len(palavra)) #Visual de boas vindas
print(palavra) #Print de boas vindas
print("-"*len(palavra,))

palavra = "|Cardápio|"
print("-"*len(palavra)) 
print(palavra) #Print do cardápio
print("-"*len(palavra)) 

print("Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais.")
print("Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais.")
print("Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais.\n") #Cardápio com quebra de linha




acumulador = 0 #Variável que acumula o valor total do pedido
while True: #Loop para o pedido
    sabor = input("Digite o sabor do produto (CP/AC): ").upper() #Sabor do produto .upper() para transformar em maiúsculo o que usuário digitar
    if sabor != "CP" and sabor != "AC":
        print("Sabor inválido. Tente novamente")
        continue #Se o sabor for diferente de CP e AC, dar print da mensagem e continuar o loop
    tamanho = input("Digite o tamanho do produto (P/M/G): ").upper()
    if tamanho != "P" and tamanho != "M" and tamanho != "G": 
        print("Tamanho inválido. Tente novamente") 
        continue 
    if sabor == "CP" and tamanho == "P": #Condição para o sabor CP e tamanho P
        acumulador += 9 #Acumulador para o sabor CP e tamanho P
    elif sabor == "CP" and tamanho == "M":
        acumulador += 14
    elif sabor == "CP" and tamanho == "G":
        acumulador += 18
    elif sabor == "AC" and tamanho == "P":
        acumulador += 11
    elif sabor == "AC" and tamanho == "M":
        acumulador += 16
    elif sabor == "AC" and tamanho == "G":
        acumulador += 20
    AlgoMais = input("Deseja pedir mais alguma coisa? (S/N): ").upper() 
    if AlgoMais == "N": #Se a resposta for N, quebrar o loop
        break
print(f"O valor total do pedido é: R${acumulador:.2f}")
