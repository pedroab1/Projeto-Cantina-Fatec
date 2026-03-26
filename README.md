# [cite_start]Controle da Cantina - Fatec Rio Claro [cite: 5]

[cite_start]Projeto desenvolvido para as disciplinas de "Estrutura de Dados" e "Linguagem de Programação 2"[cite: 4]. 

O sistema simula o funcionamento da cantina da faculdade. [cite_start]Ele controla o estoque dos produtos (priorizando os mais velhos) [cite: 9][cite_start], registra os pagamentos feitos via PIX [cite: 12] [cite_start]e gera relatórios de consumo[cite: 24]. [cite_start]Toda a base de dados foi construída usando Listas Encadeadas feitas do zero, sem utilizar as estruturas built-in do Python[cite: 27].

## Como rodar o programa

1. [cite_start]Instale a biblioteca Faker, que é usada para gerar dados aleatórios de teste[cite: 21]:
   `pip install faker`

2. Execute o arquivo principal no terminal:
   `python main_cantina.py`

[cite_start]O sistema criará o estoque inicial, fará vendas simuladas e salvará tudo em um arquivo `.pkl` para não perder os dados[cite: 22].
