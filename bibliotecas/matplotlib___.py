# Importa a biblioteca matplotlib usando um álias(apelido): plt
import matplotlib.pyplot as plt  # Biblioteca usada para criar gráficos e visualizações. Neste caso, usamos o módulo pyplot.

estudantes = ["João", "Luana", "Pedro"]  

notas = [8.5, 9, 6.5]  

plt.bar(x = estudantes, height = notas)  # Cria um gráfico de barras. Os nomes dos estudantes (lista "estudantes") são colocados no eixo X e as notas (lista "notas") definem a altura das barras.

plt.show()  # Exibe o gráfico criado na tela.
