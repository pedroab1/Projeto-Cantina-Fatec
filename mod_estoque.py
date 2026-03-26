from datetime import date

class ItemCantina:
    def __init__(self, desc, custo, venda):
        self.desc = desc
        self.custo = custo
        self.venda = venda

class LoteItem:
    def __init__(self, cod_lote, item, dt_compra, dt_vencimento, qtd):
        self.cod_lote = cod_lote
        self.item = item
        self.dt_compra = dt_compra
        self.dt_vencimento = dt_vencimento
        self.qtd = qtd
        self.prox = None

class ControleEstoque:
    def __init__(self):
        self.cabeca = None

    def inserir_lote(self, novo_lote):
        if self.cabeca == None or novo_lote.dt_vencimento < self.cabeca.dt_vencimento:
            novo_lote.prox = self.cabeca
            self.cabeca = novo_lote
            return

        temp = self.cabeca
        while temp.prox != None and temp.prox.dt_vencimento < novo_lote.dt_vencimento:
            temp = temp.prox

        novo_lote.prox = temp.prox
        temp.prox = novo_lote

    def alterar_qtd(self, cod_lote, nova_qtd):
        temp = self.cabeca
        while temp != None:
            if temp.cod_lote == cod_lote:
                temp.qtd = nova_qtd
                return
            temp = temp.prox

    def deduzir_estoque(self, desc_item, qtd_necessaria):
        total = 0
        temp = self.cabeca
        while temp != None:
            if temp.item.desc == desc_item:
                total = total + temp.qtd
            temp = temp.prox

        if total < qtd_necessaria:
            return False

        falta = qtd_necessaria
        temp = self.cabeca
        while temp != None and falta > 0:
            if temp.item.desc == desc_item:
                if temp.qtd >= falta:
                    temp.qtd = temp.qtd - falta
                    falta = 0
                else:
                    falta = falta - temp.qtd
                    temp.qtd = 0
            temp = temp.prox
        return True