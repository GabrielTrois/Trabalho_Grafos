class CarroDeLixo:
    def __init__(self, quantidade_lixo, quantidade_funcionarios, vertice_atual):
        self.quantidade_lixo = quantidade_lixo
        self.quantidade_funcionarios = quantidade_funcionarios
        self.vertice_atual = vertice_atual

    def print_info(self):
        print("Carro de Lixo:")
        print(f"Quantidade de Lixo: {self.quantidade_lixo}")
        print(f"Quantidade de Funcionarios: {self.quantidade_funcionarios}")
        print(f"Localizado no Vertice: {self.vertice_atual + 1}")