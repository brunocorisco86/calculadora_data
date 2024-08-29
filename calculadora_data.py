import datetime
import locale

# Definir o locale para pt_BR (Português do Brasil)
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

# Obter a data atual
data_atual = datetime.datetime.now()
hoje = data_atual.strftime('%d/%m/%y')
hoje_dia = data_atual.strftime('%A')  # Nome do dia da semana em português

# Calcular o número da semana
numero_da_semana = data_atual.isocalendar()[1]

print(f"Hoje é: {hoje} | {hoje_dia} | Número da semana: {numero_da_semana}\n")

# Função para obter a data do usuário e calcular o número da semana
def obter_numero_da_semana():
    while True:  # Loop contínuo até o usuário decidir sair
        # Solicitar data no formato ddmmaa
        data_str = input("Digite a data que quer informações no formato ddmmaa: ")

        try:
            # Converter a string para uma data no formato ddmmaa
            data = datetime.datetime.strptime(data_str, '%d%m%y')

            # Calcular o número da semana
            numero_da_semana = data.isocalendar()[1]

            # Obter o nome do dia da semana em português
            nome_dia_semana = data.strftime('%A')

            # Formatar a data para dd/mm/aa
            data_formatada = data.strftime('%d/%m/%y')

            # Exibir o número da semana junto com a data no formato dd/mm/aa e o nome do dia da semana
            print(f"\nData: {data_formatada} | Dia da Semana: ({nome_dia_semana})\n"
                  f"\n********************\n"
                  f"     Semana {numero_da_semana}     \n"
                  f"********************")

            # Chamar função para calcular diferença de datas
            calcular_diferenca_datas(data)

        except ValueError:
            # Mensagem de erro caso o formato da data seja inválido
            print("\nFormato de data inválido! Por favor, insira a data no formato ddmmaa.")

        # Perguntar ao usuário se deseja inserir outra data
        resposta = input("\nDeseja inserir outra data? (S/N): ").strip().upper()
        if resposta != 'S':
            print("Encerrando o programa...")
            break

# Função para calcular a diferença entre as datas
def calcular_diferenca_datas(data_usuario):
    # Calcular a diferença entre a data inserida e a data atual
    diferenca = data_usuario - data_atual

    if diferenca.days > 0:
        print(f"\nA data inserida está no futuro.")
        dias = diferenca.days
        semanas = dias // 7
        meses = dias // 30
        anos = dias // 365

        print(f"Faltam para a data...\n{dias} dias\nou {semanas} semanas\nou {meses} meses\nou {anos} anos.")
    else:
        print(f"\nA data inserida está no passado.")
        dias = abs(diferenca.days)
        semanas = dias // 7
        meses = dias // 30
        anos = dias // 365

        print(f"Se passaram desde a data...\n{dias} dias\nou {semanas} semanas\nou {meses} meses\nou {anos} anos.")

# Chamar a função
obter_numero_da_semana()

# Manter o terminal aberto
input("\nPressione Enter para fechar o programa...")
