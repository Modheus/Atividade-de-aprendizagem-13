#Aluno: Matheus Henrique

from conversor import *
while True:
  try:
    cms = float(input('Digite o valor em centímetros: '))
    break
  except:
    continue
converter(cms)