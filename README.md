# Calculadora de Diferença de Datas

Este é um script Python que permite ao usuário inserir uma data e obter informações sobre a diferença entre essa data e a data atual. O programa calcula e exibe a quantidade de dias, semanas, meses e anos faltantes ou que já se passaram, dependendo se a data está no futuro ou no passado.

## Funcionalidades

- **Exibe a data atual**: Mostra a data de hoje no formato `dd/mm/aa`, o nome do dia da semana em português e o número da semana do ano.
- **Cálculo de diferença de datas**: Permite que o usuário insira uma data no formato `ddmmaa` e calcula a diferença em dias, semanas, meses e anos em relação à data atual.
- **Loop contínuo**: Após calcular a diferença de datas, o programa pergunta ao usuário se ele deseja inserir outra data, permitindo múltiplas consultas sem precisar reiniciar o programa.

## Requisitos

- Python 3.x
- Configuração de locale para `pt_BR` (Português do Brasil). Certifique-se de que o seu sistema tem o suporte necessário para o locale `pt_BR.utf8`.

## Como Usar

1. Clone este repositório ou baixe os arquivos.

2. Certifique-se de que você tem o Python 3.x instalado em sua máquina. Você pode verificar executando:

    ```bash
    python --version
    ```

3. Execute o script com o comando:

    ```bash
    calculadora_data.py
    ```

4. O programa exibirá a data atual, o nome do dia da semana e o número da semana.

5. Você será solicitado a inserir uma data no formato `ddmmaa`. Após inserir a data, o programa calculará a diferença em relação à data atual.

6. Após cada consulta, o programa perguntará se você deseja inserir outra data. Digite `S` para continuar ou `N` para sair.

## Executável para Windows

Agora também disponibilizamos uma versão executável para Windows. Você pode encontrá-la na pasta `dist`. Siga os passos abaixo para usar:

1. Baixe o arquivo executável do diretório `dist`.
2. Dê um duplo clique no executável `calculadora_data.exe`.
3. Siga as instruções da interface, semelhante ao uso descrito acima.

## Exemplo de Uso

```bash
Hoje é: 29/08/24 | Quinta-feira | Número da semana: 35

Digite a data que quer informações no formato ddmmaa: 250625

Data: 25/06/25 | Dia da Semana: (Quarta-feira)

********************
     Semana 26     
********************

A data inserida está no futuro.
Faltam para a data...
301 dias
ou 43 semanas
ou 10 meses
ou 0 anos.

Deseja inserir outra data? (S/N): S
