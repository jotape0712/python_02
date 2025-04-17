notas = [6, 9.3, 7.7]  
qualitativo = 0.5

# Utiliza a função `map` para aplicar a função lambda em cada elemento da lista `notas`
media_atualizada = map(lambda x: x + qualitativo, notas)

# Converte o objeto `map` para uma lista
media_atualizada = list(media_atualizada)

print(media_atualizada)