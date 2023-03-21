
#input do usuário
texto = input("digite um texto qualquer: ")
texto_invertido = ""

#função para inverter caracteres de uma string
def inverter_texto(texto):

  tamanho_texto = len(texto)
  novo_texto = ""
  lista_chars = []

  #preecher a lista de caracteres com as letras do texto
  for c in range(0, tamanho_texto):
    lista_chars.append(texto[c])

  #preencher o novo texto para retornar 
  while tamanho_texto > 0:
    tamanho_texto-=1
    novo_texto += lista_chars[tamanho_texto]

  return novo_texto

#atribuir e imprimir texto invertido
texto_invertido = inverter_texto(texto)
print(texto_invertido)
