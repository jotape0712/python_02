
notas = [10, 9.3, 7.7, 5.7] # Lista chamada 'notas', contendo os valores das notas de um aluno.


def media(lista): # Definição de uma função chamada 'media', que aceita um parâmetro chamado 'lista'.
    
    calculo = sum(lista) / len(lista) # Calcula a soma dos valores da lista e divide pelo número total de elementos, encontrando a média.
    calculo = round(calculo,1) # ROUND serve para arredondar o valor, nesse caso deixou somente com uma casa decimal.
    print(calculo)

# Chama a função 'media' passando a lista 'notas' como argumento
media(notas)