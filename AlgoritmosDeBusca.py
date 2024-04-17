from ConfiguracaoNo import ConfiguracaoNo

class Busca:
    def __init__(self, teste):
        self.teste = teste
        self.estado = ConfiguracaoNo(teste.estado_inicial)
        self.explorados = []
        self.expandidos = []

    def busca_em_largura(self):
        borda = [self.estado]

        while borda:
            no = borda.pop(0)
            self.explorados.append(no.estado)

            if self.teste.objetivo(no.estado):
                return no.solucao(no.caminho())

            for filho in no.explorar(self.teste):
                if filho.estado not in self.explorados:
                    borda.append(filho)
                    self.expandidos.append(filho.estado)

        return None

    def busca_em_profundidade(self):
        borda = [self.estado]

        while borda:
            no = borda.pop()
            print("Explorando:", no.estado)

            self.explorados.append(no.estado)

            if self.teste.objetivo(no.estado):
                print("Objetivo encontrado!")
                return no.solucao(no.caminho())

            for filho in reversed(no.explorar(self.teste)):
                if filho.estado not in self.explorados:
                    print("Adicionando filho à borda:", filho.estado)
                    borda.append(filho)

        return None

    def busca_de_custo_uniforme(self):
        borda = [self.estado]
    
        while borda:
            no = borda.pop(0)
            print("Explorando estado:", no.estado)
    
            self.explorados.append(no.estado)
    
            if self.teste.objetivo(no.estado):
                print("Objetivo encontrado:", no.estado)
                return no.solucao(no.caminho())
    
            for filho in no.explorar(self.teste):
                if filho.estado not in self.explorados:
                    print("Adicionando filho à borda:", filho.estado)
                    filho.set_custo(no.custo + filho.custo)
                    borda.append(filho)
                    self.expandidos.append(filho.estado)
    
            borda.sort(key=lambda x: x.custo)
            print("Borda atualizada:", [n.estado for n in borda])
    
        return None

    def busca_a_estrela(self):
        borda = [self.estado]
    
        while borda:
            no = borda.pop(0)
            self.explorados.append(no.estado)
            print("Explorando nó:", no.estado)
    
            if self.teste.objetivo(no.estado):
                return no.solucao(no.caminho())
    
            for filho in no.explorar(self.teste):
                borda.append(filho)
                self.expandidos.append(filho.estado)
                borda.sort(key=lambda x: x.custo + self.teste.heuristica(x.estado))
                print("Borda:", [n.estado for n in borda])
    
        return None