
#RESPOSTA 2

#infomar um número
numero_informado = int(input("informe um número: "))

#variavel para guardar a mensagem ao usuário
mensagem_final = ""

#variavel para guardar a sequencia fibonnaci
sequencia = []

#FUNÇÕES

#esta funcao calcula a sequencia de fibonnaci e retorna um array com os números
def calcular_sequencia_fibonnaci(numero):

  indice0 = 0
  indice1 = 1
  ultimo_indice = indice0 + indice1
  
  sequencia_fibonnaci = [indice0, indice1, ultimo_indice]

  for c in range(numero):
    indice0 = indice1
    indice1 = ultimo_indice
    ultimo_indice = indice0 + indice1
    sequencia_fibonnaci.append(ultimo_indice)

  return sequencia_fibonnaci

#esta função testa se há o numero na sequencia fibonnaci
def teste_numero(numero, sequencia):
  
  for pos in sequencia:
    
    if (pos == numero):
      return True

  return False
      
#define uma nova sequencia e atribui a uma variavel
sequencia = calcular_sequencia_fibonnaci(numero_informado)

#imprimir a sequencia mais a mensagem final
print(sequencia)

if (teste_numero(numero_informado, sequencia)):
  mensagem_final = f"O número {numero_informado} pertence a sequência fibonnaci!"
else:
  mensagem_final = f"O número {numero_informado} não pertence a sequência fibonnaci!"

print(mensagem_final)