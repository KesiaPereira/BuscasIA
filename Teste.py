class Teste:
    def __init__(self, estado_inicial, estado_final):
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.mapa_romenia = {
            "Arad": {"Sibiu": 140, "Zerind": 75, "Timisoara": 118},
            "Zerind": {"Arad": 75, "Oradea": 71},
            "Oradea": {"Zerind": 71, "Sibiu": 151},
            "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
            "Timisoara": {"Arad": 118, "Lugoj": 111},
            "Lugoj": {"Timisoara": 111, "Mehadia": 70},
            "Mehadia": {"Lugoj": 70, "Drobeta": 75},
            "Drobeta": {"Mehadia": 75, "Craiova": 120},
            "Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
            "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
            "Fagaras": {"Sibiu": 99, "Bucharest": 211},
            "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
            "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
            "Giurgiu": {"Bucharest": 90},
            "Urziceni": {"Bucharest": 85, "Vaslui": 142, "Hirsova": 98},
            "Hirsova": {"Urziceni": 98, "Eforie": 86},
            "Eforie": {"Hirsova": 86},
            "Vaslui": {"Iasi": 92, "Urziceni": 142},
            "Iasi": {"Vaslui": 92, "Neamt": 87},
            "Neamt": {"Iasi": 87},
        }

    def acoes(self, estado):
        conexoes = self.mapa_romenia.get(estado, {})
        return list(conexoes.keys())

    def objetivo(self, estado):
        return estado == self.estado_final

    def heuristica(self, estado):
        distancias = {
            "Arad": 366, "Zerind": 374, "Oradea": 380, "Sibiu": 253, "Timisoara": 329,
            "Lugoj": 244, "Mehadia": 241, "Drobeta": 242, "Craiova": 160, "Rimnicu Vilcea": 193,
            "Fagaras": 176, "Pitesti": 100, "Bucharest": 0, "Giurgiu": 77, "Urziceni": 80,
            "Hirsova": 151, "Eforie": 161, "Vaslui": 199, "Iasi": 226, "Neamt": 234
        }
        return distancias.get(estado, 0)

    def get_mapa_romenia(self):
        return self.mapa_romenia