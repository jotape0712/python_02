notas_jurados = [88.9, 85.0, 95.2, 93.2, 90.1] # Lista contendo as notas dos 5 jurados
maior = max(notas_jurados) 
menor = min(notas_jurados) 

notas_jurados.remove(maior) # Elimina a maior nota
notas_jurados.remove(menor) # Elimina a menor nota

media_atleta = sum(notas_jurados) / len(notas_jurados) # Soma as 3 notas que restaram e faz a media delas.
media_atleta = round(media_atleta, 2) # Limita a duas casas decimais depois da virgula.

print(f"Nota da manobra: {media_atleta}")
