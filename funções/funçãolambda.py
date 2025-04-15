N1 = float(input("Digite a 1ª nota do(a) estudante: "))
N2 = float(input("Digite a 2ª nota do(a) estudante: "))
N3 = float(input("Digite a 3ª nota do(a) estudante: "))



# Uma função lambda é uma função anônima, ou seja, não precisa ser definida com def.
media_ponderada = lambda x, y, z: (x * 3 + y * 2 + z * 5) / 10   # x, y e z são os três valores que serão passados para a função.


media_estudante = media_ponderada(N1, N2, N3)  # Aqui, a função media_ponderada é chamada, usando as notas inseridas (N1, N2, N3) como argumentos. O resultado será armazenado em media_estudante.


print(media_estudante)      