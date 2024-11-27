class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("trintrin")
    def parar(self):
        print("Parou")
    def correr(self) :
        print("Vruuummm")
    def __str__(self) -> str:
        return f"A bicicleta tipo {self.modelo} é da cor {self.cor}, custa {self.valor}, do ano de {self.ano}"

bike_1 = Bicicleta("Preta", "Monark", 2010, 100)
bike_2 = Bicicleta("Vermelho", "Mountain Bike", 2024, 1000)

bike_1.buzinar()
bike_2.correr()
bike_1.correr()

print(bike_1.valor)
print(bike_1)
print(bike_2)
