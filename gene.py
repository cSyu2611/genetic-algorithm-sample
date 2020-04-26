from decimal import Decimal
import params

class gene_status: #遺伝子情報(0,1)のリストとその遺伝子の評価値をもつクラス

    genes, evl = None, None #遺伝子の優劣リスト, 遺伝子の評価値

    def __init__(self, genes, evl):
        self.genes = genes
        self.evl = evl

    def get_genes(self): #遺伝子情報をリターン
        return self.genes

    def get_evl(self): #遺伝子情報の評価値を格納
        return self.evl

    def set_genes(self,genes):
        self.genes = genes

    def set_evl(self):
        genes_total = sum(self.genes)
        self.evl = Decimal(genes_total) / Decimal(params.GENE_LENGTH)