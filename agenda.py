class agenda:
    def exibir_menu():
        '''exibe menu de opções do sistema''' #docstring, documentta a funcionalidade da função
        print("Agenda de contatos")
        print("(1) Criar novo contato")
        print("(2) Listar todos os contatos")
        print("(3) Buscar contato")



    def cadastrar_contato(nome, telefone, email, arquivo_agenda):
        agenda = open(arquivo_agenda, 'a')
        agenda.write(f'{nome}, {telefone}, {email}\r')
        agenda.close()

    #Teste de cadastro
    # cadastrar_contato("Little Stuart", "555 33231", "stuarlittle@desenho.com", "agenda.csv")
    # cadastrar_contato("Jhon Mayer", "555 87745", "jhonmayer@hotmail.com", "agenda.csv")
    # cadastrar_contato("Don Ramon", "333 45675", "donramon@hotmail.com", "agenda.csv")

    # Validação do cadastro:
    agenda = open("agenda.csv", 'r')
    contatos = agenda.readlines() #contatos em lita
    # for contato in contatos:
    #     print(contato)

    def listar_contatos(arquivo_agenda):
        agenda = open(arquivo_agenda, 'r')
        contatos = agenda.read() #Contatos é uma string
        contatos = contatos.splitlines() # contatos é uma lista onde cada elemento é um dos contatos.
        agenda.close() #fechar arquivo

        print(f"{'Contato':<30}\t{' Telefone':<20}\t{' E-mail':<30}")
        for contato in contatos:
            contato = contato.split(',') #contato é uma lista contendo 3 elementos: nome, telefone, e-mail
            nome = contato[0]
            telefone = contato[1]
            email = contato[2]
            print(f"{nome:<30}\t{telefone:<20}\t{email:<30}")

    #listar_contatos("agenda.csv")

    def buscar_contato(busca, arquivo_agenda):
        resultado = 0
        agenda = open(arquivo_agenda, 'r')
        contatos = agenda.read()
        contatos = contatos.splitlines()
        for contato in contatos:
            contato = contato.split(',')
            nome, telefone, email = contato[0], contato[1], contato[2]
            if busca in nome or busca in telefone or busca in email:
                print(f"{nome:30} {telefone:20} {email:50}")
                resultado += 1
        print(f"\nForam encontrados {resultado} resultado(s).")