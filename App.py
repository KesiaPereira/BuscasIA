from Teste import Teste
from AlgoritmosDeBusca import Busca

class App:
    def main(self):
        teste = Teste("Arad", "Bucharest")
        busca = Busca(teste)

        print("\n---Métodos de busca para encontrar o caminho de Arad à Bucharest---")

        print("\nBusca em Largura:")
        print(busca.busca_em_largura())

        print("\nBusca em Profundidade:")
        print(busca.busca_em_profundidade())

        print("\nBusca de Custo Uniforme:")
        print(busca.busca_de_custo_uniforme())

        print("\nBusca A*:")
        print(busca.busca_a_estrela())

if __name__ == "__main__":
    app = App()
    app.main()
