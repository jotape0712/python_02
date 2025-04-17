import os
import random

print("Seja Bem-vindo ao Jokempo!")
opções = ["1", "2", "3"]

while True:
    print("""Escolha seu ataque: 
    1: Pedra
    2: Papel
    3: Tesoura""")

    jogador = input("Escolha: ")
    maquina = random.choice(opções)

    if jogador == "1" and maquina == "1":
        print("Você jogou: Pedra")
        print("Seu oponente jogou: Pedra")
        print("Empate!")
        
    elif jogador == "1" and maquina == "2":
        print("Você jogou: Pedra")
        print("Seu oponente jogou: Papel")
        print("Você perdeu!")

    elif jogador == "2" and maquina == "3":
        print("Você jogou: Papel")
        print("Seu oponente jogou: Tesoura")
        print("Você perdeu!")

    elif jogador == "3" and maquina == "1":
        print("Você jogou: Tesoura")
        print("Seu oponente jogou: Pedra")
        print("Você perdeu!")

    elif jogador == "1" and maquina == "3":
        print("Você jogou: Pedra")
        print("Seu oponente jogou: Tesoura")
        print("Você ganhou!")

    elif jogador == "2" and maquina == "1":
        print("Você jogou: Papel")
        print("Seu oponente jogou: Pedra")
        print("Você ganhou!")

    elif jogador == "3" and maquina == "2":
        print("Você jogou: Tesoura")
        print("Seu oponente jogou: Papel")
        print("Você ganhou!")