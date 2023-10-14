#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao #usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então #exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.#


def controladorPrestacao():
  contador = 0
  valorTotal = 0
  valorPrestacao = 0
  resposta = 'S'
  while resposta == 'S':
    valorPrestacao = entradaDados()
    contador += 1
    valorTotal = valorPrestacao + valorTotal
    print(contador, valorTotal)
    resposta = coletarResposta()
  impressaoFinal(valorTotal, contador)
    
def entradaDados():
  valorPrestacao = float(input('\nDigite o valor da prestação: '))
  diasAtraso = int(input('\nDigite os dias de atraso: ')) 
  valorPrestacao = calcularPrestacao(valorPrestacao, diasAtraso)
  return valorPrestacao
  
def calcularPrestacao(valorPrestacao, diasAtraso):
  if diasAtraso == 0:
    valorPrestacao = exibirPrestacaoEmDia(valorPrestacao)
    return valorPrestacao
  else:
    valorPrestacaoEmAtraso = exibirPrestacaoEmAtraso(valorPrestacao, diasAtraso)
    return valorPrestacaoEmAtraso
  

def exibirPrestacaoEmDia(valorPrestacao):
  print(f'\nO valor da Prestação é R$ ', valorPrestacao)
  return valorPrestacao

def exibirPrestacaoEmAtraso(valorPrestacao, diasAtraso):
  multa = valorPrestacao * 0.03
  juros = valorPrestacao * 0.001 * diasAtraso
  valorPrestacaoComJuros = valorPrestacao + multa + juros
  print(f'\nO valor da Prestacao é R$ ',{valorPrestacaoComJuros})
  return valorPrestacaoComJuros  
  
def coletarResposta():
  resposta = input('\nDeseja continuar? (S/N) ').upper()
  return resposta

def impressaoFinal(valorTotal, contador):
  print(f'\nO valor total de prestações é R$ {valorTotal}')
  print(f'\nO total de prestações pagas foram {contador}')
  
#Programa Principal
controladorPrestacao()
