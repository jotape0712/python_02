
nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')] # Lista de tuplas feita anteriormente.
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]] # Lista de lista feita anteriormente.
medias = [9.0, 7.3, 5.8, 6.7, 8.5]  # Lista feita anteriormente.


for i in range(len(nomes)): # Passa por todos os elementos de "nomes".


              # [resultado_if IF cond ELSE resultado_else FOR item IN lista]
    situacao = ["Aprovado(a)!" if media >=6 else "Reprovado(a)!" for media in medias] 
    print(nomes[i][0], "está", situacao[i])
    # O nomes[i] pega o elemento na posição i da lista nomes e o [0] seleciona o primeiro item da tupla.
    # O situacao[i] acessa o elemento correspondente à posição atual (i) do loop for.

