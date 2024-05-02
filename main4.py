palavra = "|Bem vindo a livraria do Allan Crissanto|" 
print("-"*len(palavra)) #Visual de boas vindas
print(palavra) #Print de boas vindas
print("-"*len(palavra))

lista_livro = [] #Lista de livros vazia
id_global = 0 #Variável global para o id do livro

def cadastrar_livro(id): #Função criada para cadastrar livro com parâmetro id
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    livro = {"id":id, "nome":nome, "autor":autor, "editora":editora} #Dicionário criado para o livro
    lista_livro.append(livro) #.append() para adicionar o livro na lista de livros

def consultar_livro(): #Função criada para consultar livro
    while True: #Loop para a consulta
        opcao = input("Qual opção deseja?\n 1. Consultar Todos\n 2. Consultar por Id\n 3. Consultar por Autor\n 4. Retornar ao menu:\n ")
        if opcao == "1":
            for livro in lista_livro:
                for key, value in livro.items():
                    print(f"{key}: {value}") #Se opção for 1, printar todos os livros
        elif opcao == "2":
            id = int(input("Digite o id do livro: "))
            for livro in lista_livro:
                if livro["id"] == id:
                    for key, value in livro.items():
                        print(f"{key}: {value}") #Se opção for 2, printar o livro com o id digitado
        elif opcao == "3":
            autor = input("Digite o autor do livro: ")
            for livro in lista_livro:
                if livro["autor"] == autor:
                    for key, value in livro.items():
                        print(f"{key}: {value}") #Se opção for 3, printar o livro com o autor digitado
        elif opcao == "4":
            break #Se opção for 4, quebrar o loop
        else:
            print("Opção inválida") #Se opção for diferente de 1, 2, 3 e 4, printar a mensagem

def remover_livro(): #Função criada para remover livro
    while True:
        id = int(input("Digite o id do livro para ser removido: "))
        for livro in lista_livro:
            if livro["id"] == id:
                lista_livro.remove(livro) #Se o id digitado for igual ao id do livro, remover o livro da lista de livros
                print('Livro removido com sucesso')
                break #Quebrar o loop
        else:
            print("Id inválido")
            continue #Se o id digitado for diferente do id do livro, dar print da mensagem e continuar o loop
        break

while True:
    opcao = input("Qual opção deseja?\n 1. Cadastrar Livro\n 2. Consultar Livro\n 3. Remover Livro \n 4. Encerrar Programa:\n ")
    if opcao == "1": #Se opção for 1, chamar a função cadastrar_livro
        id_global += 1 #Incrementar o id_global
        cadastrar_livro(id_global) #Chamar a função cadastrar_livro com o parametro id_global
    elif opcao == "2":
        consultar_livro() #Se opção for 2, chamar a função consultar_livro
    elif opcao == "3":
        remover_livro() #Se opção for 3, chamar a função remover_livro
    elif opcao == "4": #Se opção for 4, encerrar o programa e consequentemente quebrar o loop
        break 
    else:
        print("Opção inválida")
        continue #Se opção for diferente de 1, 2, 3 e 4, dar print da mensagem e continuar o loop

print("Programa encerrado")
