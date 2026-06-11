# Dicionário global para armazenar os dados dos jogadores
jogadores = {}

def cadastrar_jogador(nome):
    if nome in jogadores:
        print(f"❌ Erro: O jogador '{nome}' já está cadastrado.")
    else:
        jogadores[nome] = {"saldo": 0.0, "extrato": []}
        print(f"✅ Jogador '{nome}' cadastrado com sucesso!")

def creditar(nome, valor):
    if nome in jogadores:
        if valor > 0:
            jogadores[nome]["saldo"] += valor
            jogadores[nome]["extrato"].append(f"+ R$ {valor:.2f} (Crédito)")
            print(f"💰 Crédito de R$ {valor:.2f} realizado para '{nome}'. Novo saldo: R$ {jogadores[nome]['saldo']:.2f}")
        else:
            print("❌ Erro: O valor do crédito deve ser maior que zero.")
    else:
        print(f"❌ Erro: Jogador '{nome}' não encontrado.")

def debitar(nome, valor):
    if nome in jogadores:
        if valor > 0:
            if jogadores[nome]["saldo"] >= valor:
                jogadores[nome]["saldo"] -= valor
                jogadores[nome]["extrato"].append(f"- R$ {valor:.2f} (Débito)")
                print(f"💸 Débito de R$ {valor:.2f} realizado para '{nome}'. Novo saldo: R$ {jogadores[nome]['saldo']:.2f}")
            else:
                print("❌ Erro: Saldo insuficiente para realizar este débito.")
        else:
            print("❌ Erro: O valor do débito deve ser maior que zero.")
    else:
        print(f"❌ Erro: Jogador '{nome}' não encontrado.")

def exibir_extrato(nome):
    if nome in jogadores:
        print(f"\n--- Extrato de {nome} ---")
        if not jogadores[nome]["extrato"]:
            print("Nenhuma movimentação registrada.")
        else:
            for transacao in jogadores[nome]["extrato"]:
                print(transacao)
        print(f"Saldo atual: R$ {jogadores[nome]['saldo']:.2f}")
        print("-------------------------\n")
    else:
        print(f"❌ Erro: Jogador '{nome}' não encontrado.")

def menu():
    while True:
        print("\n=== Banco do Jogo de Tabuleiro ===")
        print("1. Cadastrar Jogador")
        print("2. Creditar (Adicionar dinheiro)")
        print("3. Debitar (Retirar dinheiro)")
        print("4. Exibir Extrato")
        print("5. Sair do Jogo")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            nome = input("Digite o nome do jogador: ").strip()
            cadastrar_jogador(nome)

        elif opcao == '2':
            nome = input("Digite o nome do jogador que vai receber o dinheiro: ").strip()
            try:
                valor = float(input("Digite o VALOR para CREDITAR: R$ "))
                creditar(nome, valor)
            except ValueError:
                print("❌ Erro: Por favor, digite um número válido (ex: 150.50).")

        elif opcao == '3':
            nome = input("Digite o nome do jogador que vai pagar/perder dinheiro: ").strip()
            try:
                valor = float(input("Digite o VALOR para DEBITAR: R$ "))
                debitar(nome, valor)
            except ValueError:
                print("❌ Erro: Por favor, digite um número válido.")

        elif opcao == '4':
            nome = input("Digite o nome do jogador para ver o extrato: ").strip()
            exibir_extrato(nome)

        elif opcao == '5':
            print("Encerrando o sistema do banco... Bom jogo!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()