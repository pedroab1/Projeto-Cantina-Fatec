from datetime import datetime

class PgtoPix:
    def __init__(self, cliente, perfil, formacao, valor):
        self.cliente = cliente
        self.perfil = perfil
        self.formacao = formacao
        self.valor = valor
        self.data_hora = datetime.now()

class NoPgto:
    def __init__(self, id_pgto, info_pgto):
        self.id_pgto = id_pgto
        self.info_pgto = info_pgto
        self.prox = None

class HistoricoPgto:
    def __init__(self):
        self.cabeca = None

    def add_pgto(self, novo_no):
        if self.cabeca == None:
            self.cabeca = novo_no
        else:
            temp = self.cabeca
            while temp.prox != None:
                temp = temp.prox
            temp.prox = novo_no