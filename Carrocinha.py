class Carrocinha:
    def __init__(self, quantidade_animais, vertice_atual):
        self.quantidade_animais = quantidade_animais
        self.vertice_atual = vertice_atual

    def print_info(self):
        print("Carrocinha:")
        print(f"Quantidade de Animais: {self.quantidade_animais}")
        print(f"Localizada no Vertice: {self.vertice_atual + 1}")