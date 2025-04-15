
notas = [10, 9.3, 7.7, 5.7] 

 

def boletim(lista):  # Define uma função chamada boletim, que receberá uma lista de notas como entrada

    media = sum(notas) / len(notas)  # Então sum(notas) / len(notas) divide a soma das notas pelo número total de notas, calculando assim a média do estudante.
    media = round(media,1)           # round(media, 1): arredonda o valor da média para uma casa decimal, para que fique mais legível    

    if media >= 7:
        situação = "Aprovado(a)"
    else:
        situação = "Reprovado(a)"
    
    return (media, situação)   # Aqui a função entrega dois resultados: A media final e a situação do estudante!

media, situação = boletim(notas)  # Executamos a função que foi criada e armazenamos as variaveis que foram entregues.

print(f"O(a) estudante atingiu a media {media} e foi {situação}!")
    
