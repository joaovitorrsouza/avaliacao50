""""exe1
lista_nomes = ['João','Vinicius','Felipe','Jorge','Caíque']
print(lista_nomes)
lista_idade = ['21','41','54','12','76']
print(lista_idade)
"""""
"""""exe2
lista_nomes = ['João','Vinicius','Felipe','Jorge','Caíque']
lista_nomes.append(["Victor" ,"Luana"])
print(lista_nomes)
"""
"""""exe3
nome  = (input("Digite seu nome:"))
nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
nota3 = float(input("Digite a nota 3:"))
media_final = float (nota1 + nota2 + nota3)/3

if media_final >=7:
    print(f"Sua média é: {media_final}")
    print("Aprovado")
else:
    print(f"Sua média é: {media_final}")
    print("Reprovado")
"""

"""""exe4
salario = float(input("Digite o seu salário:"))
Percentual_INSS = 7.5/100
Percentual_INSS2 = 9/100
Percentual_INSS3 = 12/100
Percentual_INSS4 = 14/100
desconto_INSS = salario * Percentual_INSS;
desconto_INSS2 = salario * Percentual_INSS2;
desconto_INSS3 = salario * Percentual_INSS3;
desconto_INSS4 = salario * Percentual_INSS4;
salario_liquido = (salario - Percentual_INSS);
salario_liquido2 = (salario - Percentual_INSS2);
salario_liquido3 = (salario - Percentual_INSS3);
salario_liquido4 = (salario - Percentual_INSS4);

if salario == 1212:
    print(f"Foram descontados {desconto_INSS} do seu salário por conta do INSS")
    print(f"Seu salário líquido é de: {salario_liquido}")
if salario >= 1212.01 and salario <= 2427.35:
    print(f"Foram descontados {desconto_INSS2} do seu salário por conta do INSS")
    print(f"Seu salário líquido é de: {salario_liquido2}")
if salario >= 2427.36 and salario <= 3641.03:
    print(f"Foram descontados {desconto_INSS3} do seu salário por conta do INSS")
    print(f"Seu salário líquido é de: {salario_liquido3}")
if salario >= 3641.04 and salario <= 7087.22:
    print(f"Foram descontados {desconto_INSS4} do seu salário por conta do INSS")
    print(f"Seu salário líquido é de: {salario_liquido4}")
"""




"""""exe5
print("Digite dois valores:")
a = int(input())
b = int(input())
c = input("Qual cálculo deseja fazer:Soma , Subtração , Multiplicação ou Divisão:")
if c == "Soma":
    print("Resultado:" , a+b)
if c == "Subtração":
    print("Resultado:" , a-b)
if c == "Multiplicação":
    print("Resultado:" , a*b)
if c == "Divisão":
    print("Resultado:", a/b)
"""""
"""""exe6
def menu_inicial():
  print('Programa para Conversão de Temperaturas')
  print('1. Converter de Celsius para Fahrenheit')
  print('2. Converter de Fahrenheit para Celsius')

def cel_fahr():
  C = float(input('Entre com a temperatura em graus Celsius: '))
  F = C * (9 / 5) + 32
  print('Valor em Fahrenheit: {0}°F'.format(F))

def fahr_cel():
  F = float(input('Entre com a temperatura em graus Fahrenheit: '))
  C = (F - 32) * (5 / 9)
  print('Valor em Celsius: {0}°C'.format(C))

if __name__ == '_main_':
  menu_inicial()
  escolha = input('Escolha o tipo de conversão que deseja realizar: ')

  if escolha == '1':
    cel_fahr()

  if escolha == '2':
    fahr_cel()
"""

"""""exe7
nome  = (input("Digite seu nome:"))
trab4 = float(input("Digite a nota do trabalho:"))
teste3 = float(input("Digite a nota do teste:"))
prova5 = float(input("Digite a nota da prova:"))

media_pond = (trab4 * 4) + (teste3 * 3) + (prova5 * 5)/4 + 3 + 5;
"""
"""""exe8
tabuada=int(input("Tabuada do numero: "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))
pergunta = input("Deseja uma nova tabuada?")
while pergunta == 'Sim':
    tabuada = int(input("Tabuada do numero: "))

    for count in range(10):
        print("%d x %d = %d" % (tabuada, count + 1, tabuada * (count + 1)))
    pergunta = input("Deseja uma nova tabuada?")
else:
    print("Você saiu")
"""












