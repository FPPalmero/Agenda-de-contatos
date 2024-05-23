#####################################################################################################
def adicionar_contato(nome_contato, telefone_contato, email_contato, lista_contatos):
    try:
        if len(str(telefone_contato)) != 11:
            raise ValueError ("O número de telefone deve ter 11 digitos. ")
        if "@" not in email_contato and "." not in email_contato:
            raise ValueError ("Digite um endereço de email válido. ")
        
        contato = {
            "nome": nome_contato,
            "telefone": telefone_contato,
            "email": email_contato,
            "favorito": False
        }
        lista_contatos.append(contato)
        print(f"O contato {nome_contato} foi adicionado com sucesso à sua lista de contatos.")
    except ValueError as error:
        print(f"Erro ao adicionar contato: {error}")


#####################################################################################################
def ver_contatos(lista_contatos):
    print(f"\nLista de contatos: ")

    try:
        if not lista_contatos:
            raise ValueError ("Não há nenhum contato adicionado à sua lista de contatos.")
        
        for indice, contato in enumerate(lista_contatos):
            status = "★" if contato["favorito"] else " "
            nome_contato = contato["nome"]
            telefone_contato = contato["telefone"]
            email_contato = contato["email"]
            print(f"{indice + 1}.[{status}] Nome: {nome_contato}. Telefone: {telefone_contato}. Email: {email_contato}")
    except ValueError as error:
        print(f"Erro ao visualizar contatos: {error}")
    return


#####################################################################################################
def editar_contato(indice, lista_contatos):
    try:
        indice = int(indice) - 1

        if indice < 0 or indice >= len(lista_contatos):
            raise IndexError ("O índice fornecido não é válido.")
        
        print("Escolha o que deseja editar: ")
        print("1.Nome")
        print("2. Telefone")
        print("3. Email")
        alteracao = input("Qual alteração deseja fazer? ")

        if alteracao == "1":
            alterar_nome = input("Insira o novo nome: ")
            lista_contatos[indice]["nome"] = alterar_nome
            print("Alteração realizada com sucesso")

        elif alteracao == "2":
            alterar_telefone = int(input("Insira o novo telefone: "))
            lista_contatos[indice]["telefone"] = alterar_telefone
            print("Alteração realizada com sucesso")

        elif alteracao == "3":
            alterar_email = input("Insira o novo email: ")
            lista_contatos[indice]["email"] = alterar_email
            print("Alteração realizada com sucesso")

        else:
            print("Insira uma opção válida")

    except IndexError as error:
        print(f"Erro ao editar contato: {error}")
    return
    

#####################################################################################################
def favoritar_contato(indice, lista_contatos):
    indice = int(indice) - 1
    lista_contatos[indice]["favorito"] = True
    print(f"Contato adicionado aos favoritos")
    return


#####################################################################################################
def contatos_favoritos(lista_contatos):
    favoritos = []

    for contato in lista_contatos:
        if contato["favorito"]:
            favoritos.append(contato["nome"])

    if favoritos:
        print("Os contatos favoritos são: ")
        for i in favoritos:
            print(f"Nome: {i}")
    else:
        print("Não há contatos favoritos.")
    return


#####################################################################################################
def apagar_contato(indice,lista_contatos):
    indice = int(indice) - 1
    if indice >= 0 and indice < len(lista_contatos):
        remover_contato = lista_contatos.pop(indice)
        print(f"Contato {remover_contato['nome']} removido com sucesso.")
    return


#####################################################################################################
lista_de_contatos = []

while True:
    print("\nAgenda de Contatos: ")
    print("1. Adicionar contato: ")
    print("2. Visualizar contatos: ")
    print("3. Editar contato: ")
    print("4. Favoritar contato: ")
    print("5. Ver contatos favoritos: ")
    print("6. Apagar contato: ")


    opcao = input("\nInsira o que deseja fazer: ")

    if opcao == "1":
        nome = input("Insira o nome do contato: ")
        telefone = int(input("Insira seu telefone: "))
        email = input("Insira seu email: ")
        adicionar_contato(nome, telefone, email, lista_de_contatos)

    if opcao == "2":
        ver_contatos(lista_de_contatos)

    if opcao == "3":
        ver_contatos(lista_de_contatos)
        indice_contato = input("Insira o número do contato que deseja atualizar: ")
        editar_contato(indice_contato,lista_de_contatos)

    if opcao == "4":
        ver_contatos(lista_de_contatos)
        indice_contato = input("Insira o número do contato que deseja favoritar: ")
        favoritar_contato(indice_contato, lista_de_contatos)

    if opcao == "5":
        contatos_favoritos(lista_de_contatos)

    if opcao == "6":
        ver_contatos(lista_de_contatos)
        remover_contato = int(input("Insira o número do contato que deseja remover: "))
        apagar_contato(remover_contato,lista_de_contatos)