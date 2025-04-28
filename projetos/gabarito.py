
gabarito = ['D', 'A', 'B', 'C', 'A']

respostas_estudantes = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'B', 'C', 'A'], ['D', 'B', 'A', 'A', 'A']]

notas = [] 
for respostas in respostas_estudantes:
        nota = 0
        for i in range(len(gabarito)):
            if respostas[i] == gabarito[i]:
                nota += 1 
            if not respostas[i] in gabarito:
                raise ValueError(f"Alternativa'{respostas[i]}' invalida!")
        notas.append(nota)
        

try:
    print(notas)
except ValueError as e:
     print(e)

else:
    print(notas)









        
        



