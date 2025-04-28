
def media(lista: list=[0]) -> float: # Transforma a lista em um dado "float".
  
  
  calculo = sum(lista) / len(lista)

  if len(lista) > 4:
    raise ValueError("A lista não pode conter mais do que 4 notas!") # Raise cria a sua própria exceção para um determinado comportamento. ( raise NomeDoErro("Mensagem"))

  return calculo

try: # código a ser executado. Caso uma exceção seja lançada, pare imediatamente.
  notas = [6, 7, 8, 5]
  resultado = media(notas)
except TypeError: # Se uma exceção for lançada no try, rode esse código, senão pule esta etapa.
  print("Só são aceitos valores numéricos!")
except ValueError as e: # Exceção 2.
  print(e)
else: # Se não houver uma exeção lançada pelo try, rode essa parte.
  print(resultado)
finally: # Rode essa parte (com ou sem exceção).
  print("A consulta foi encerrada!")
