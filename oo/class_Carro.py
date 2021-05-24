"""
Criar um Carro seguindo os conceitos de orientação a objeto:

Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

* Motor
* Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

* Atributo de dado velocidade
* Método acelerar, que deverá incremetar a velocidade de uma unidade
* Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

* Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
* Método girar_a_direita
* Método girar_a_esquerda
"""

# Objeto veículo:
class Carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao


# Objeto Motor:
class Motor:
    def __init__(self, velocidade):
        self.velocidade = velocidade

    def acelerar(self):
       pass

    def frear(self):
        pass


# Objeto Direção:
class Direcao:
    def __init__(self, sentido):
        self.sentido = sentido

    def girar_a_direita(self):
        pass

    def gira_a_esquerda(self):
        pass


# Instanciando os objetos:
carro = Carro()
motor = Motor()
direcao = Direcao()