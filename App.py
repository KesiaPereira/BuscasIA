from Teste import Teste
from AlgoritmosDeBusca import Busca

class App:
    def main(self):
        teste = Teste("Arad", "Bucharest")
        busca = Busca(teste)

        print("\nResultado da busca de custo uniforme:")
        print(busca.busca_de_custo_uniforme())

if __name__ == "__main__":
    app = App()
    app.main()
