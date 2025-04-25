
nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]  # Lista de tuplas feita anteriormente.
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]  # Lista de listas feita anteriormente.
medias = [9.0, 7.3, 5.8, 6.7, 8.5]  # Lista de médias feita anteriormente.

# dict comprehension: cria um dicionário {nome: situação}
situacoes = {nomes[i][0]: "Aprovado(a)!" if medias[i] >= 6 else "Reprovado(a)!" for i in range(len(nomes))}
# nomes[i][0] -> pega o nome da pessoa (primeiro elemento da tupla).
# medias[i] -> pega a média correspondente.
# "Aprovado(a)!" if medias[i] >= 6 else "Reprovado(a)!" -> define a situação com base na média.


for nome, status in situacoes.items():
    print(nome, "está", status)

