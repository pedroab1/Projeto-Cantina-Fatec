import pickle
import random
from datetime import datetime, date
from faker import Faker
from mod_estoque import ItemCantina, LoteItem, ControleEstoque
from mod_pagamento import PgtoPix, NoPgto, HistoricoPgto

class RegistroConsumo:
    def __init__(self, id_reg, cliente, item, qtd, total):
        self.id_reg = id_reg
        self.cliente = cliente
        self.item = item
        self.qtd = qtd
        self.total = total
        self.data_hora = datetime.now()
        self.prox = None

class ListaConsumo:
    def __init__(self):
        self.cabeca = None

    def add_consumo(self, novo_no):
        novo_no.prox = self.cabeca
        self.cabeca = novo_no

class AppCantina:
    def __init__(self, estoque_inicial):
        self.estoque = estoque_inicial
        self.pgtos = HistoricoPgto()
        self.consumos = ListaConsumo()
        self.id_venda = 1

    def achar_item(self, desc_item):
        temp = self.estoque.cabeca
        while temp != None:
            if temp.item.desc == desc_item:
                return temp.item
            temp = temp.prox
        return None

    def processar_venda(self, cliente, perfil, formacao, desc_item, qtd):
        if self.estoque.deduzir_estoque(desc_item, qtd) == True:
            item_obj = self.achar_item(desc_item)
            valor_final = item_obj.venda * qtd

            novo_pgto = PgtoPix(cliente, perfil, formacao, valor_final)
            no_p = NoPgto(self.id_venda, novo_pgto)
            self.pgtos.add_pgto(no_p)

            no_c = RegistroConsumo(self.id_venda, cliente, item_obj, qtd, valor_final)
            self.consumos.add_consumo(no_c)

            self.id_venda = self.id_venda + 1
            return True
        return False

    def exibir_vendas(self):
        print("\n--- RELATORIO DE VENDAS ---")
        temp = self.pgtos.cabeca
        soma = 0
        while temp != None:
            p = temp.info_pgto
            print(f"ID: {temp.id_pgto} | Nome: {p.cliente} | Tipo: {p.perfil} | Curso: {p.formacao} | R$: {p.valor:.2f}")
            soma = soma + p.valor
            temp = temp.prox
        print(f"Total arrecadado: R$ {soma:.2f}")

    def exibir_consumo(self):
        print("\n--- RELATORIO DE CONSUMO ---")
        temp = self.consumos.cabeca
        while temp != None:
            print(f"ID: {temp.id_reg} | Cliente: {temp.cliente} | Produto: {temp.item.desc} | Qtd: {temp.qtd} | R$: {temp.total:.2f}")
            temp = temp.prox

def guardar_dados(app, nome_arq="dados_app.pkl"):
    arq = open(nome_arq, "wb")
    pickle.dump(app, arq)
    arq.close()

def ler_dados(nome_arq="dados_app.pkl"):
    try:
        arq = open(nome_arq, "rb")
        app = pickle.load(arq)
        arq.close()
        return app
    except FileNotFoundError:
        return None

def gerar_faker(app, quantidade):
    f = Faker("pt_BR")
    opcoes_itens = ["Biscoito", "Suco de Uva"]
    
    for i in range(quantidade):
        nome_falso = f.name()
        tipo_falso = random.choice(["Aluno", "Servidor", "Professor"])
        curso_falso = random.choice(["IA", "ESG"])
        item_falso = random.choice(opcoes_itens)
        app.processar_venda(nome_falso, tipo_falso, curso_falso, item_falso, 1)

if __name__ == "__main__":
    meu_app = ler_dados()

    if meu_app == None:
        estq = ControleEstoque()
        meu_app = AppCantina(estq)

        item1 = ItemCantina("Biscoito", 2.00, 4.00)
        item2 = ItemCantina("Suco de Uva", 3.00, 5.00)

        loteA = LoteItem(101, item1, date.today(), date(2026, 10, 10), 40)
        loteB = LoteItem(102, item2, date.today(), date(2026, 8, 20), 30)

        estq.inserir_lote(loteA)
        estq.inserir_lote(loteB)

        gerar_faker(meu_app, 15)

    meu_app.exibir_vendas()
    meu_app.exibir_consumo()
    
    guardar_dados(meu_app)