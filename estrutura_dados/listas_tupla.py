
from random import randint

estudantes = ["Joao", "Pedro", "Luana", "Jose", "Caio", "Neymar"]

def gerar_codigo():
    return str(randint(0,999)) # O número é convertido em str para que possamos juntar esse número com outra informação, como letras ou nomes.


codigo_estudante = []

for i in range(len(estudantes)): # Esse comando percorre os índices da lista de estudantes
    codigo_estudante.append((estudantes[i], estudantes[i][0] + gerar_codigo()))  # () Adiciona uma tupla à lista. Cada tupla tem duas partes: sempre o nome e o código gerado.

print(codigo_estudante)

# Tuplas são pacotes que, depois de criada, não pode ser modificada.



