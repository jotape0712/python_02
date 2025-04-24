

notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

def media(lista: list=[0]) -> float: # Define a lista "notas" como "lista" e altera para float.
    calculo = sum(lista) / len(lista) # Faz o calculo da media
    return calculo

                 # EXP for ITEN in LISTA
medias = [round(media(nota),1) for nota in notas] # Esta linha utiliza uma list comprehension para calcular a média de cada sublista em notas, arredondando o valor para uma casa decimal.


nomes = [('Joao', 'J648'), ('Pedro', 'P720'), ('Luana', 'L639'), ('Jose', 'J475'), ('Caio', 'C738'), ('Neymar', 'N397')] # Lista criada no "Lista_tupla.py".

nomes = [nome[0] for nome in nomes] # Utilizamos uma list comprehension para extrair apenas os nomes dos estudantes, ignorando os códigos.

 

estudantes_media = list(zip(nomes, medias)) # A função zip combina duas listas: nomes e medias. O resultado é uma lista de tuplas que associa cada estudante à sua respectiva média
# Usar "list" para criar lista explícita (em vez de apenas um iterável).


candidatos = [estudante[0] for estudante in estudantes_media if estudante[1] >= 8.0] # Outra list comprehension é usada aqui para filtrar os nomes dos estudantes cuja média é maior ou igual a 8.0. Somente os nomes desses estudantes são adicionados à lista candidatos.

print(candidatos)