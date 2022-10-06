def converter(cm):
  valor_pl = cm/2.54
  print (valor_pl)
  file = open('arquivo.txt', 'a+', encoding = 'utf-8')
  file.write(f'o valor {cm} em centímetros corresponde a %.3f valor em polegadas.\n' %(valor_pl))