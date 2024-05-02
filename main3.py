palavra = "|Bem vindo a copiadora do Allan Crissanto|"
print("-"*len(palavra)) #Visual de boas vindas
print(palavra) #Print de boas vindas
print("-"*len(palavra))


def escolha_servico(): #Função criada para a escolha do serviço
    while True: #Loop para a escolha do serviço
        servico = input("Digite o serviço desejado.\n DIG - Digitalização\n ICO - Impressão Colorida\n IPB - Impressão Preto e Branco\n FOT - Fotocópia\n ").upper() #Escolha do serviço .upper() para transformar o que o usuário digitar em maiúsculo
        if servico == "DIG": #Se o usuário digitar DIG, retornar o valor do serviço
            return 1.10 #Retorno do valor do serviço
        elif servico == "ICO":
            return 1
        elif servico == "IPB":
            return 0.40
        elif servico == "FOT":
            return 0.20
        else:
            print("Serviço inválido. Entre com um serviço válido.")
            continue #Se o serviço for diferente de DIG, ICO, IPB e FOT, dar print da mensagem e continuar o loop

def num_pagina(): #Função criada para o número de páginas
    while True:
        try: #"tentar" para o número de páginas
            num_pagina = int(input("Digite o número de páginas: "))
            if num_pagina < 20: #Se o número de páginas for menor que 20, retornar o número de páginas sem desconto
                return num_pagina
            elif num_pagina >= 20 and num_pagina < 200: #Se o número de páginas for maior ou igual a 20 e menor que 200, retornar o número de páginas com 15% de desconto
                return num_pagina * 0.85
            elif num_pagina >= 200 and num_pagina < 2000:
                return num_pagina * 0.80
            elif num_pagina >= 2000 and num_pagina < 20000:
                return num_pagina * 0.75
            else:
                print("Não aceitamos essa quantidade de número de páginas. Tente novamente")
                continue #Se o número de páginas for maior que 20000, dar print da mensagem e continuar o loop
        except:
            print("Número de páginas inválido. Tente novamente")
            continue #Se o número de páginas não for um número, dar print da mensagem e continuar o loop

def servico_extra(): #Função criada para o serviço extra
    while True:
        extra = input("Digite o serviço adicional.\n 1 - Encardenação Simples.\n 2 - Encardenação Capa Dura. \n 0 - Não desejo mais nada.\n ")
        if extra == "1":
            return 15 #Se a opção digitada por 1, retornar o valor do serviço extra
        elif extra == "2":
            return 40
        elif extra == "0":
            return 0 #Se a opção digitada por 0, o usuário não deseja mais nada
        else:
            print("Serviço adicional inválido. Tente novamente")
            continue #Se a opção digitada for diferente de 1, 2 e 0, dar print da mensagem e continuar o loop

#Programa Principal

servico = escolha_servico() #Variável servico recebe a função escolha_servico
num_pag = num_pagina() #Variável num_pag recebe a função num_pagina
extra = servico_extra() #Variável extra recebe a função servico_extra
total = (servico * num_pag) + extra #Variável total recebe o cálculo do valor total a pagar
print(f"O valor total a pagar é: R${total:.2f} (serviço: R${servico:.2f} * número de páginas: {num_pag} + extra: R${extra:.2f})")
