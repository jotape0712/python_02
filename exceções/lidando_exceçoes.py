
notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0], 
 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

try: # código a ser executado. Caso uma exceção seja lançada, pare imediatamente
    nome = input("Digite o nome do estudante: ") 
    resultado = notas[nome]
except KeyError: # Se uma exceção for lançada no try, rode esse código, senão pule esta etapa
    print("Estudante não matriculado!")
else: # Se não houver uma exeção lançada pelo try, rode essa parte
    print(resultado)
finally: # Rode essa parte (com ou sem exceção)
    print("A consulta foi encerrada!")



