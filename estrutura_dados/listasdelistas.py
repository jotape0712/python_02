
notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0,   # Lista que contém os nomes dos alunos alternados com suas notas
               'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0,   
               'Ana', 6.0, 10.0, 9.5]


nome = [] # Lista para armazenar apenas os nomes dos alunos
notas_juntas = [] # Lista para armazenar apenas as notas dos alunos


for i in range(len(notas_turma)):  # Loop para percorrer todos os elementos da lista notas_turma
    if i % 4 == 0:  # A cada 4 elementos, o primeiro será o nome do aluno
        nome.append(notas_turma[i])  # Adiciona o nome à lista nome
    else:  
        notas_juntas.append(notas_turma[i])  # Adiciona a nota à lista notas_juntas

# Lista para armazenar as notas organizadas por aluno
notas = []


for i in range(0, len(notas_juntas), 3):  
    notas.append([notas_juntas[i], notas_juntas[i+1], notas_juntas[i+2]])  # O range(0, len(notas_juntas), 3) significa que i começa em 0 e avança de 3 em 3. Ou seja, ele pega o primeiro elemento (i), depois o quarto, o sétimo, e assim por diante.
 # notas_juntas[i], notas_juntas[i+1] e notas_juntas[i+2] pegam três notas consecutivas e as colocam juntas em notas.


# Imprime a lista de notas organizadas por aluno
print(notas)

# Imprime a lista de notas do primeiro aluno
print(notas[0])

# Imprime apenas a primeira nota do primeiro aluno
print(notas[0][0])