#Controle da Cantina - Fatec Rio Claro

Projeto desenvolvido para as disciplinas de "Estrutura de Dados" e "Linguagem de Programação 2". 

O sistema simula o funcionamento da cantina da faculdade. Ele controla o estoque dos produtos (priorizando os mais velhos), registra os pagamentos feitos via PIX e gera relatórios de consumo. Toda a base de dados foi construída usando Listas Encadeadas feitas do zero, sem utilizar as estruturas built-in do Python.

## Como rodar o programa

1.Instale a biblioteca Faker, que é usada para gerar dados aleatórios de teste:
   `pip install faker`

2. Execute o arquivo principal no terminal:
   `python main_cantina.py`

O sistema criará o estoque inicial, fará vendas simuladas e salvará tudo em um arquivo `.pkl` para não perder os dados.
