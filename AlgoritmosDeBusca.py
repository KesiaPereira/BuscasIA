from ConfiguracaoNo import Node

class Busca:
    def __init__(self, problema):
        self.problema = problema
        self.estado = Node(problema.get_estado_inicial())
        self.explorados = []
        self.expandidos = []

    def busca_em_largura(self):
        borda = [self.estado]

        while borda:
            no = borda.pop(0)
            self.explorados.append(no.get_estado())

            if self.problema.objetivo(no.get_estado()):
                return no.solucao(no.caminho())

            for filho in no.explorar(self.problema):
                if filho.get_estado() not in self.explorados:
                    borda.append(filho)
                    self.expandidos.append(filho.get_estado())

        return None

    def busca_em_profundidade(self):
        borda = [self.estado]

        while borda:
            no = borda.pop()
            self.explorados.append(no.get_estado())

            if self.problema.objetivo(no.get_estado()):
                return no.solucao(no.caminho())

            for filho in no.explorar(self.problema):
                if filho.get_estado() not in self.explorados:
                    borda.append(filho)
                    self.expandidos.append(filho.get_estado())

        return None

    def busca_de_custo_uniforme(self):
        borda = [self.estado]

        while borda:
            no = borda.pop(0)
            self.explorados.append(no.get_estado())

            if self.problema.objetivo(no.get_estado()):
                return no.solucao(no.caminho())

            for filho in no.explorar(self.problema):
                if filho.get_estado() not in self.explorados:
                    filho.set_custo(no.get_custo() + filho.get_custo())
                    borda.append(filho)
                    self.expandidos.append(filho.get_estado())
                    borda.sort(key=lambda x: x.get_custo())

        return None

    def busca_a_estrela(self):
        borda = [self.estado]

        while borda:
            no = borda.pop(0)
            self.explorados.append(no.get_estado())

            if self.problema.objetivo(no.get_estado()):
                return no.solucao(no.caminho())

            for filho in no.explorar(self.problema):
                borda.append(filho)
                self.expandidos.append(filho.get_estado())
                borda.sort(key=lambda x: x.get_distancia_percorrida() + x.get_heuristica(self.problema))

        return None
