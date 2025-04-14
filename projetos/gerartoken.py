
from random import randint  # Importa o metodo RANDINT da biblioteca random

nome = input("Digite aqui seu nome: ")

while True: # Cria um loop para que o print só entre em ação quando o IF for verdadeiro.
    
    token = randint(1000, 9998) # RANDINT é um metodo que gera um valor inteiro aleatorio, no caso entre 1000 e 9998.

    if token % 2 == 0: 
        print(f"Olá {nome}, o seu token de acesso é {token}. Seja bem-vindo!")
        

        break

# O token só gera codigos com valores pares!