class Celular:
    def __init__(self, modelo, marca, preco, chip):
        self.modelo = modelo
        self.marca = marca
        self.preco = preco
        self.__chip = chip

    def __str__(self):
        return f"Informações:\nModelo: {self.modelo}\nMarca: {self.marca}\nPreço: {self.preco}\nChip: {self.__chip}"

c1 = Celular("S24", "Samsung", 4500, "Snapdragon")

print(c1)
