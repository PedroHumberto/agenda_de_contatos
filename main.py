from agenda import agenda


arquivo_agenda = input("Informe o arquivo da agenda: ")
while True:
    agenda.exibir_menu()
    print("-----------------------------\n")
    opcao = int(input("Selecione a opção desejada (digite 9 para sair): "))
    print("-----------------------------\n")
    if opcao == 1:
        print("Cadastro Novo Contato.")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        agenda.cadastrar_contato(nome, telefone, email, arquivo_agenda)
        print(f'\nContato {nome} cadastrado com sucesso.')
        print("-----------------------------\n")
    elif opcao == 2:
        print("Listar todos os contatos da agenda")
        agenda.listar_contatos(arquivo_agenda)
        print("-----------------------------\n")
    elif opcao == 3:
        print("Buscar contato.")
        busca = input("Informe o parâmetro de busca: ")
        agenda.buscar_contato(busca,arquivo_agenda)
        print("-----------------------------\n")
    elif opcao == 9:
        break
    else:
        print("Opção inválida.")
        print("**********************************\n")







