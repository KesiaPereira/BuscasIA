class Node:
    def __init__(self, estado, pai, acao, custo):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def no_filho(self, problema, acao):
        proximo_estado = problema.transicao(self.estado, acao)
        custo_filho = problema.custo(self.estado, acao, proximo_estado)
        return Node(proximo_estado, self, acao, custo_filho)

    def explorar(self, problema):
        nos = []
        for acao in problema.acoes(self.estado):
            nos.append(self.no_filho(problema, acao))
        return nos

    def caminho(self):
        caminho = []
        no_atual = self
        while no_atual:
            caminho.insert(0, no_atual)
            no_atual = no_atual.pai
        return caminho

    def solucao(self, caminho):
        solucao = []
        for node in caminho:
            solucao.append(node.estado)
        return solucao
