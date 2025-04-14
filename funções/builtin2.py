
notas = {'1º Bimestre': 9.0, '2º Bimestre': 7.7, '3º Bimestre': 9.2}

soma = sum(notas.values()) # SUM é uma built-in utilizada para somar os elementos de um iterável, como uma lista, dicionario ou conjunto.

qtd_notas = len(notas) # LEN é uma built-in utilizada para contar a quantidade de algo.

media = soma / qtd_notas
media = round(media,1)  # ROUND é uma built-in utilizada para arredondar um valor.

print(f"Sua media do ano foi de {media}!")