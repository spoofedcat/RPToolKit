#!/usr/bin/env python3
import os
import sys 
from time import sleep

#Criação das funções das Megas Garantias conforme o seu tipo ou familia, 
#por ex: Grandes Domésticos, peq. domesticos, telemoveis, imagem e som, etc...
#Algumas funções são comuns a várias familias diferentes, pois as Megas partilham os mesmos codigos

#Grandes Domesticos - ampliação até 5 anos.
def MG_electrodomesticos_5_anos():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108098 --> 39€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 500:
    print("\033[1;35;40mMG - 9108099 --> 59€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 750:
    print("\033[1;35;40mMG - 9108100 --> 79€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 1000:
    print("\033[1;35;40mMG - 9108101 --> 89€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 1500:
    print("\033[1;35;40mMG - 9108102 --> 99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108103 --> 119€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 5000:
    print("\033[1;35;40mMG - 9108104 --> 159€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val > 5000:
    print("Só válido para equipamentos até 5000€")
    q = input("")
    os.system('clear')
  return MG_electrodomesticos_5_anos

#Grandes Domesticos - ampliação até 3 anos.
def MG_electrodomesticos_3_anos():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 100:
    print("\033[1;35;40mMG - 9108167 --> 15€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108168 --> 20€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108169 --> 25€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108170 --> 30€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 750:
    print("\033[1;35;40mMG - 9108171 --> 35€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 900:
    print("\033[1;35;40mMG - 9108172 --> 40€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 1200:
    print("\033[1;35;40mMG - 9108173 --> 45€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 1200:
    print("\033[1;35;40mMG - 9108174 --> 50€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val > 1200:
    print("Só válido para equipamentos até 1200€")
    q = input("")
    os.system('clear')
  return MG_electrodomesticos_3_anos

#Grandes Domesticos - Cozinha Completa
def MG_eletrodomesticos_deb_direto_cozinha_completa():
  print("\033[1;37;45mDébito Mensal - Cozinha Completa")
  print("\033[1;35;40m1 - \033[1;37;40mCozinha Completa 3 peças")
  print("\033[1;35;40m2 - \033[1;37;40mCozinha Completa 4 peças\n")
  val = int(input(""))
  if val == 1:
    os.system('clear')
    print("\033[1;37;45mDébito Mensal - Cozinha Completa 3 peças")
    print("\033[1;35;40mMG - 9108191 - 14,99€")
    q = input("")
    os.system('clear')
  elif val == 2:
    os.system('clear')
    print("\033[1;37;45mDébito Mensal - Cozinha Completa 4 peças")
    print("\033[1;35;40mMG - 9108192 - 17,99€")
    q = input("")
    os.system('clear')
  else:
    os.system('clear')
  return MG_eletrodomesticos_deb_direto_cozinha_completa()
  
#Grandes Domesticos - Ar Condicionado
def MG_eletrodomesticos_deb_direto_ar_condicionado():
  os.system('clear')
  print("\033[1;37;45mDébito Mensal - Ar Condicionado")
  print("\033[1;35;40mMG - 9108197 - 13,99€")
  q = input("")
  os.system('clear')
  return MG_eletrodomesticos_deb_direto_ar_condicionado
  
#Pequenos Domésticos - Troca Direta
def MG_troca_direta_peq_dom_1_ano():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 25:
    print("\033[1;35;40mMG - 9108226 --> 4,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 50:
    print("\033[1;35;40mMG - 9108227 --> 10,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 75:
    print("\033[1;35;40mMG - 9108228 --> 14,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 100:
    print("\033[1;35;40mMG - 9108229 --> 18,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 125:
    print("\033[1;35;40mMG - 9108230 --> 21,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 150:
    print("\033[1;35;40mMG - 9108231 --> 24,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val > 150:
    print("A troca direta só pode ser efetuada em artigos até 150€")
    print("Para artigos superiores a este valor, utilize a modalidade\nSPV 1 ano")
    print("Avançar para esta opção? S/N:\n")
    val = str(input(""))
    if val == ('s') or val == ('S'):
      MG_electrodomesticos_3_anos()
    elif val == 'n' or 'N':
      os.system('clear')
    return MG_troca_direta_peq_dom_1_ano

#Imagem e som - Ampliar até 5 anos
def MG_imagem_som_5_anos_n_portatil():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108105 --> 39€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 500:
    print("\033[1;35;40mMG - 9108106 --> 59€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 750:
    print("\033[1;35;40mMG - 9108107 --> 79€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 1000:
    print("\033[1;35;40mMG - 9108108 --> 89€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 1500:
    print("\033[1;35;40mMG - 9108109 --> 99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108110 --> 119€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 5000:
    print("\033[1;35;40mMG - 9108111 --> 219€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val > 5000:
    print("Só válido para equipamentos até 5000€")
    q = input("")
    os.system('clear')
  return MG_imagem_som_5_anos_n_portatil
    
#Imagem e som não portatil - Proteção Total 3 Anos  
def MG_imagem_som_3_anos_n_portatil():        
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108126 --> 39€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Dano Acidental.")
    print("    Roubo ou furto no 1º ano.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 500:
    print("\033[1;35;40mMG - 9108127 --> 59€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Dano Acidental.")
    print("    Roubo ou furto no 1º ano.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 750:
    print("\033[1;35;40mMG - 9108128 --> 79€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Dano Acidental.")
    print("    Roubo ou furto no 1º ano.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 1000:
    print("\033[1;35;40mMG - 9108129 --> 89€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Dano Acidental.")
    print("    Roubo ou furto no 1º ano.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 1500:
    print("\033[1;35;40mMG - 9108130 --> 109€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Dano Acidental.")
    print("    Roubo ou furto no 1º ano.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108131 --> 129€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Dano Acidental.")
    print("    Roubo ou furto no 1º ano.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 5000:
    print("\033[1;35;40mMG - 9108132 --> 169€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Dano Acidental.")
    print("    Roubo ou furto no 1º ano.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val > 5000:
    print("Só válido para equipamentos até 5000€")
    q = input("")
    os.system('clear')
  return MG_imagem_som_3_anos_n_portatil
  
#Imagem e som portatil - Ampliar para 3 anos  
def MG_imagem_som_3_anos_portatil():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108133 --> 39€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 500:
    print("\033[1;35;40mMG - 9108134 --> 59€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 750:
    print("\033[1;35;40mMG - 9108135 --> 79€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 1000:
    print("\033[1;35;40mMG - 9108136 --> 89€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 1500:
    print("\033[1;35;40mMG - 9108137 --> 109€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108138 --> 129€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 5000:
    print("\033[1;35;40mMG - 9108139 --> 139€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val > 5000:
    print("Só válido para equipamentos até 5000€")
    q = input("")
    os.system('clear')
  return MG_imagem_som_3_anos_portatil

#Imagem e som portatil e não portatil - Ampliar garantia por mais um ano
def MG_imagem_som_SPV_1_ano():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 100:
    print("\033[1;35;40mMG - 9108167 --> 15€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <=250:
    print("\033[1;35;40mMG - 9108168 --> 20€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108169 --> 25€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108170 --> 30€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 750:
    print("\033[1;35;40mMG - 9108171 --> 35€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 900:
    print("\033[1;35;40mMG - 9108172 --> 40€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 1200:
    print("\033[1;35;40mMG - 9108173 --> 45€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 1500:
    print("\033[1;35;40mMG - 9108174 --> 50€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val > 1500:
    print("Só válido para equipamentos até 1500€")
    q = input("")
    os.system('clear')
  return MG_imagem_som_SPV_1_ano
  
#Imagem e som portatil e não portatil - Troca direta  
def MG_imagem_som_troca_direta():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 25:
    print("\033[1;35;40mMG - 9108226 --> 4,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 50:
    print("\033[1;35;40mMG - 9108227 --> 10,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 75:
    print("\033[1;35;40mMG - 9108228 --> 14,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 100:
    print("\033[1;35;40mMG - 9108229 --> 18,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 125:
    print("\033[1;35;40mMG - 9108230 --> 21,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 150:
    print("\033[1;35;40mMG - 9108231 --> 24,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val > 150:
    print("Só válido para equipamentos até 150€")
    q = input("")
    os.system('clear')
  return MG_imagem_som_troca_direta
  
#Informatica não portatil  - Ampliar para 5 anos  
def MG_informatica_5_anos_n_portatil():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108112 --> 59€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 500:
    print("\033[1;35;40mMG - 9108113 --> 79€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 750:
    print("\033[1;35;40mMG - 9108114 --> 99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 1000:
    print("\033[1;35;40mMG - 9108115 --> 109€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 1500:
    print("\033[1;35;40mMG - 9108116 --> 129€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108117 --> 159€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 5000:
    print("\033[1;35;40mMG - 9108118 --> 179€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val > 5000:
    print("Só válido para equipamentos até 5000€")
    q = input("")
    os.system('clear')
  return MG_informatica_5_anos_n_portatil
  
#Informática Portatil - Ampliar para 5 anos  
def MG_informatica_5_anos_portatil():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108119 --> 69€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 500:
    print("\033[1;35;40mMG - 9108120 --> 99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 750:
    print("\033[1;35;40mMG - 9108121 --> 139€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 1000:
    print("\033[1;35;40mMG - 9108122 --> 159€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 1500:
    print("\033[1;35;40mMG - 9108123 --> 179€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108124 --> 209€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val <= 5000:
    print("\033[1;35;40mMG - 9108125 --> 229€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Deslocação do técnico.")
    print("    Mão de obra.")
    print("    Peças e componentes.")
    print("    Em caso de impossibilidade de reparação - substituição do equipamento por 1     novo.")
    q = input("")
    os.system('clear')
  elif val > 5000:
    print("Só válido para equipamentos até 5000€")
    q = input("")
    os.system('clear')
  return MG_informatica_5_anos_portatil
  
#Informática não portatil - Proteção total 3 anos  
def MG_informatica_n_portatil_protecao_total_3_anos():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108140 --> 49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 500:
    print("\033[1;35;40mMG - 9108141 --> 69€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 750:
    print("\033[1;35;40mMG - 9108142 --> 89€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 1000:
    print("\033[1;35;40mMG - 9108143 --> 99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 1500:
    print("\033[1;35;40mMG - 9108144 --> 119€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108145 --> 149€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 5000:
    print("\033[1;35;40mMG - 9108146 --> 209€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val > 5000:
    print("Só válido para equipamentos até 5000€")
    q = input("")
    os.system('clear')
  return MG_informatica_n_portatil_protecao_total_3_anos
  
#Informática portatil - proteção total 3 anos  
def MG_informatica_portatil_protecao_total_3_anos():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108147 --> 59€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 500:
    print("\033[1;35;40mMG - 9108148 --> 89€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 750:
    print("\033[1;35;40mMG - 9108149 --> 129€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 1000:
    print("\033[1;35;40mMG - 9108150 --> 159€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 1500:
    print("\033[1;35;40mMG - 9108151 --> 179€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108152 --> 209€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 5000:
    print("\033[1;35;40mMG - 9108153 --> 309€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val > 5000:
    print("Só válido para equipamentos até 5000€")
    q = input("")
    os.system('clear')
  return MG_informatica_portatil_protecao_total_3_anos
  
#Informatica - 1 ano de cobertura de danos acidentais  
def MG_informatica_danos_acidentais_1_ano():
  print("\033[1;35;40mMG - 9108202 --> 34€")
  print("\033[1;37;40mCoberturas:\n")
  print("    Avarias elétricas ou mecânicas.")
  print("    Danos acidentais.")
  q = input("")
  os.system('clear')
  return MG_informatica_danos_acidentais_1_ano
  
#Informatica Pro - Modalidade de débito direto  
def MG_informatica_pro_debito_direto():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 300:
    print("\033[1;35;40mMG - 9108193 --> 9€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Roubo ou furto durante 1 ano.")
    print("    Danos acidentais.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108194 --> 10€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Roubo ou furto durante 1 ano.")
    print("    Danos acidentais.")
    q = input("")
    os.system('clear')
  elif val <= 900:
    print("\033[1;35;40mMG - 9108195 --> 11€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Roubo ou furto durante 1 ano.")
    print("    Danos acidentais.")
    q = input("")
    os.system('clear')
  elif val <= 1500:
    print("\033[1;35;40mMG - 9108196 --> 13€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Roubo ou furto durante 1 ano.")
    print("    Danos acidentais.")
    q = input("")
    os.system('clear')
  elif val > 1500:
    print("Só válido para equipamentos até 1500€")
    q = input("")
    os.system('clear')
  return MG_informatica_pro_debito_direto
  
#Tablets - quebra de ecrã por 2 anos  
def MG_quebra_ecra_tablets_2_anos():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <=100:
    print("\033[1;35;40mMG - 9108201 --> 34€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108185 --> 49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.")
    q = input("")
    os.system('clear')
  elif val <= 500:
    print("\033[1;35;40mMG - 9108186 --> 69€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.")
    q = input("")
    os.system('clear')
  elif val > 500:
    print("\033[1;35;40mMG - 9108187 --> 79€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.")
    q = input("")
    os.system('clear')
  return MG_quebra_ecra_tablets_2_anos
  
#Ebooks - quebra de ecrã por 2 anos  
def MG_quebra_ecra_ebooks_2_anos():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108182 --> 39€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.")
    q = input("")
    os.system('clear')
  elif val <= 500:
    print("\033[1;35;40mMG - 9108183 --> 49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.")
    q = input("")
    os.system('clear')
  elif val > 500:
    print("Só válido para equipamentos até 500€")
    q = input("")
    os.system('clear')
  return MG_quebra_ecra_ebooks_2_anos
  
#Discos Externos - danos acidentais  
def MG_danos_acidentais_2_anos_discos_externos():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 150:
    print("\033[1;35;40mMG - 9108198 --> 39€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Danos Acidentais.")
    print("    Recuperação de dados.")
    q = input("")
    os.system('clear')
  elif val <= 300:
    print("\033[1;35;40mMG - 9108199 --> 49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Danos Acidentais.")
    print("    Recuperação de dados.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108200 --> 69€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Danos Acidentais.")
    print("    Recuperação de dados.")
    q = input("")
    os.system('clear')
  elif val > 600:
    print("Só válido para equipamentos até 600€")
    q = input("")
    os.system('clear')
  return MG_danos_acidentais_2_anos_discos_externos
  
#Informatica - Ampliar para mais 1 ano de garantia  
def MG_informatica_spv_1_ano():
  val = float(input("Introduza o valor do equipamento : "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 100:
    print("\033[1;35;40mMG - 9108167 --> 15€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108168 --> 20€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108169 --> 25€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108170 --> 30€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 750:
    print("\033[1;35;40mMG - 9108171 --> 35€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 900:
    print("\033[1;35;40mMG - 9108172 --> 40€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 1200:
    print("\033[1;35;40mMG - 9108173 --> 45€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 1500:
    print("\033[1;35;40mMG - 9108174 --> 50€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val > 1500:
    print("Só válido para equipamentos até 1500€")
    q = input("")
    os.system('clear')
  return MG_informatica_spv_1_ano
  
#Informatica - troca direta  
def MG_informatica_troca_direta():
  val = float(input("Introduza o valor do equipamento : "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 25:
    print("\033[1;35;40mMG - 9108226 --> 4,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 50:
    print("\033[1;35;40mMG - 9108227 --> 10,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 75:
    print("\033[1;35;40mMG - 9108228 --> 14,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 100:
    print("\033[1;35;40mMG - 9108229 --> 18,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 125:
    print("\033[1;35;40mMG - 9108230 --> 21,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 150:
    print("\033[1;35;40mMG - 9108231 --> 24,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val > 150:
    print("Só válido para equipamentos até 150€")
    q = input("")
    os.system('clear')
  return MG_informatica_troca_direta
  
#Fotografia - proteção total 3 anos  
def MG_fotografia_prot_total_3_anos():
  val = float(input("Introduza o valor do equipamento : "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108133 --> 39€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 500:
    print("\033[1;35;40mMG - 9108134 --> 59€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 750:
    print("\033[1;35;40mMG - 9108135 --> 69€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 1000:
    print("\033[1;35;40mMG - 9108136 --> 89€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 1500:
    print("\033[1;35;40mMG - 9108137 --> 99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108138 --> 129€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val <= 5000:
    print("\033[1;35;40mMG - 9108139 --> 139€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto no 1º ano.")
    q = input("")
    os.system('clear')
  elif val > 5000:
    print("Só válido para equipamentos até 5000€")
    q = input("")
    os.system('clear')
  return MG_fotografia_prot_total_3_anos
  
#Fotografia - proteção total por 1 ano  
def MG_fotografia_prot_total_1_ano():
  val = float(input("Introduza o valor do equipamento : "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 100:
    print("\033[1;35;40mMG - 9108203 --> 16,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108204 --> 21,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto.")
    q = input("")
    os.system('clear')
  elif val >250:
    print("Só válido para equipamentos até 250€")
    q = input("")
    os.system('clear')
  return MG_fotografia_prot_total_1_ano
  
#Fotografia - aumentar garantia para mais 1 ano  
def MG_fotografia_spv_1_ano():
  val = float(input("Introduza o valor do equipamento : "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 100:
    print("\033[1;35;40mMG - 9108167 --> 15€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108168 --> 20€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108169 --> 25€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108170 --> 30€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 750:
    print("\033[1;35;40mMG - 9108171 --> 35€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 900:
    print("\033[1;35;40mMG - 9108172 --> 40€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 1200:
    print("\033[1;35;40mMG - 9108173 --> 45€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val <= 1500:
    print("\033[1;35;40mMG - 9108174 --> 50€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    q = input("")
    os.system('clear')
  elif val > 1500:
    print("Só válido para equipamentos até 1500€")
  return MG_fotografia_spv_1_ano
  
#Fotografia - troca direta  
def MG_fotografia_troca_direta():
  val = float(input("Introduza o valor do equipamento : "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 25:
    print("\033[1;35;40mMG - 9108226 --> 4,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 50:
    print("\033[1;35;40mMG - 9108227 --> 10,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 75:
    print("\033[1;35;40mMG - 9108228 --> 14,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 100:
    print("\033[1;35;40mMG - 9108229 --> 18,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 125:
    print("\033[1;35;40mMG - 9108230 --> 21,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 150:
    print("\033[1;35;40mMG - 9108231 --> 24,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Troca por equipamento igual ou semelhante ou")
    print("    Devolução do valor da compra do equipamento.")
    q = input("")
    os.system('clear')
  elif val > 150:
    print("Só válido para equipamentos até 150€")
    q = input("")
    os.system('clear')
  return MG_fotografia_troca_direta
  
#Telemoveis - proteção de quebra de ecra 1 ano  
def MG_telemoveis_quebra_ecra():
  val = float(input("Introduza o valor do equipamento : "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 50:
    print("\033[1;35;40mMG - 9108239 --> 15€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.")
    q = input("")
    os.system('clear')
  elif val <= 100:
    print("\033[1;35;40mMG - 9108240 --> 19€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.")
    q = input("")
    os.system('clear')
  elif val <= 150:
    print("\033[1;35;40mMG - 9108241 --> 29€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108242 --> 39€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108243 --> 59€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108244 --> 99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.")
    q = input("")
    os.system('clear')
  elif val > 600:
    print("\033[1;35;40mMG - 9108245 --> 119€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.")
    q = input("")
    os.system('clear')
  return MG_telemoveis_quebra_ecra
  
#Telemoveis - proteção total por 1 ano
def MG_telemoveis_plus():
  val = float(input("Introduza o valor do equipamento : "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 50:
    print("\033[1;35;40mMG - 9108253 --> 20€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.\n    Derrame de liquidos.\n    Dano acidental.\n    Roubo ou furto qualificado.\n    Cobertura mundial do sinistro.")
    q = input("")
    os.system('clear')
  elif val <= 100:
    print("\033[1;35;40mMG - 9108254 --> 24€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.\n    Derrame de liquidos.\n    Dano acidental.\n    Roubo ou furto qualificado.\n    Cobertura mundial do sinistro.")
    q = input("")
    os.system('clear')
  elif val <= 150:
    print("\033[1;35;40mMG - 9108255 --> 39€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.\n    Derrame de liquidos.\n    Dano acidental.\n    Roubo ou furto qualificado.\n    Cobertura mundial do sinistro.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108256 --> 49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.\n    Derrame de liquidos.\n    Dano acidental.\n    Roubo ou furto qualificado.\n    Cobertura mundial do sinistro.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108257 --> 79€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.\n    Derrame de liquidos.\n    Dano acidental.\n    Roubo ou furto qualificado.\n    Cobertura mundial do sinistro.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108258 --> 119€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.\n    Derrame de liquidos.\n    Dano acidental.\n    Roubo ou furto qualificado.\n    Cobertura mundial do sinistro.")
    q = input("")
    os.system('clear')
  elif val > 600:
    print("\033[1;35;40mMG - 9108259 --> 149€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.\n    Derrame de liquidos.\n    Dano acidental.\n    Roubo ou furto qualificado.\n    Cobertura mundial do sinistro.")
    q = input("")
    os.system('clear')
  return MG_telemoveis_plus
  
#Telemoveis - proteção total renovavel(débito direto)  
def MG_telemveis_plus_prot_total():
  val = float(input("Introduza o valor do equipamento : "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108264 --> 49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.\n    Derrame de liquidos.\n    Dano acidental.\n    Roubo ou furto qualificado.\n    Cobertura mundial do sinistro.\n    Cobertura de mais de 1 sinistro por ano.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108265 --> 79€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.\n    Derrame de liquidos.\n    Dano acidental.\n    Roubo ou furto qualificado.\n    Cobertura mundial do sinistro.\n    Cobertura de mais de 1 sinistro por ano.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108266 --> 119€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.\n    Derrame de liquidos.\n    Dano acidental.\n    Roubo ou furto qualificado.\n    Cobertura mundial do sinistro.\n    Cobertura de mais de 1 sinistro por ano.")
    q = input("")
    os.system('clear')
  elif val > 600:
    print("\033[1;35;40mMG - 9108267 --> 149€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã.\n    Derrame de liquidos.\n    Dano acidental.\n    Roubo ou furto qualificado.\n    Cobertura mundial do sinistro.\n    Cobertura de mais de 1 sinistro por ano.")
    print("")
    q = input("")
    os.system('clear')
  return MG_telemveis_plus_prot_total
  
#SmartWatch - proteção quebra de ecra 1 ano  
def MG_smartwatch_quebra_ecra():
  val = float(input("Introduza o valor do equipamento : "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 50:
    print("\033[1;35;40mMG - 9108232 --> 15€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã por 12 meses.")
    q = input("")
    os.system('clear')
  elif val <= 100:
    print("\033[1;35;40mMG - 9108233 --> 19€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã por 12 meses.")
    q = input("")
    os.system('clear')
  elif val <= 150:
    print("\033[1;35;40mMG - 9108234 --> 29€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã por 12 meses.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108235 --> 39€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã por 12 meses.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108236 --> 59€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã por 12 meses.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108237 --> 99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Quebra de ecrã por 12 meses.")
    q = input("")
    os.system('clear')
  elif val > 600:
    print("Só válido para equipamentos até 600€")
    q = input("")
    os.system('clear')
  return MG_smartwatch_quebra_ecra
    
#SmartWatch - proteção total 1 ano    
def MG_smartwatch_plus():
  val = float(input("Introduza o valor do equipamento : "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 50:
    print("\033[1;35;40mMG - 9108246 --> 20€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Danos acidentais.\n    Roubo ou furto.")
    q = input("")
    os.system('clear')
  elif val <= 100:
    print("\033[1;35;40mMG - 9108247 --> 24€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Danos acidentais.\n    Roubo ou furto.")
    q = input("")
    os.system('clear')
  elif val <= 150:
    print("\033[1;35;40mMG - 9108248 --> 39€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Danos acidentais.\n    Roubo ou furto.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108249 --> 49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Danos acidentais.\n    Roubo ou furto.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108250 --> 79€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Danos acidentais.\n    Roubo ou furto.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108251 --> 119€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Danos acidentais.\n    Roubo ou furto.")
    q = input("")
    os.system('clear')
  elif val > 600:
    print("Só válido para equipamentos até 600€")
    q = input("")
    os.system('clear')
  return MG_smartwatch_plus
  
#SmartWatch - proteção total 1 ano débito direto      
def MG_smartwatch_plus_prot_total():
  val = float(input("Introduza o valor do equipamento : "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 250:
    print("\033[1;35;40mMG - 9108260 --> 49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Danos acidentais.\n    Roubo ou furto.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108261 --> 79€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Danos acidentais.\n    Roubo ou furto.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108262 --> 119€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Danos acidentais.\n    Roubo ou furto.")
    q = input("")
    os.system('clear')
  elif val > 600:
    print("Só válido para equipamentos até 600€")
    q = input("")
    os.system('clear')
  return MG_smartwatch_plus_prot_total
  
#Entertenimento, Consolas - Proteção total por 3 anos  
def MG_entertenimento_prot_total_3_anos():
  print("1 - Consolas não portateis")
  print("2 - Consolas portateis")
  val = int(input(""))
  os.system('clear')
  if val == 1:
    print("\033[1;35;40mMG - 9108175 --> 49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto 1º Ano.")
    q = input("")
    os.system('clear')
  elif val == 2:
    print("\033[1;35;40mMG - 9108176 --> 59€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.")
    print("    Danos acidentais.")
    print("    Roubo ou furto 1º Ano.")
    q = input("")
    os.system('clear')
  return MG_entertenimento_prot_total_3_anos
  
#Entertenimento, Consolas - Troca direta por 3 anos    
def MG_entertenimeto_troca_direta_3_anos():
  print("\033[1;35;40mMG - 9108177 --> 39€")
  print("\033[1;37;40mCoberturas:\n")
  print("    Avarias elétricas ou mecânicas.")
  print("    Troca por equipamento igual ou semelhante ou")
  print("    Devolução do valor da compra do equipamento.")
  q = input("")
  os.system('clear')
  return MG_entertenimeto_troca_direta_3_anos
  
#Entertenimento, jogos - Sunstituição direta durante 1 ano
def MG_entertenimento_substituicao_direta_1_ano_jogos():
  val = float(input("Introduza o valor do equipamento : "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 29:
    print("\033[1;35;40mMG - 9108178 --> 1€")
    q = input("")
    os.system('clear')
  elif val <= 100:
    print("\033[1;35;40mMG - 9108179 --> 3€")
    q = input("")
    os.system('clear')
  elif val > 100:
    print("Só válido para equipamentos até 100€")
    q = input("")
    os.system('clear')
  return MG_entertenimento_substituicao_direta_1_ano_jogos
    
#Grandes Domesticos Frio - Débito Mensal
def MG_DM_linha_branca_frio():
  print("\033[1;35;40mMG - 9108273 --> 2,99€")
  print("\033[1;37;40mCoberturas:\n")
  print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias não cobertas pelo fabricante:\n    - Uso.\n    - Desgaste.\n    - Avarias provocadas pelo calcário.\n    Benefícios VIP:\n    - Três avarias iguais no período de doze meses,substituição do equipamento.\n    - Perda de alimentos refrigerados/congelados até 100€ por avaria.\n    - Reinstalação por mudança.\n    - Compromisso em tempo de reparação -> se não tiver o seu equipamento\n      reparado em menos de 10 dias úteis, será compensado com 100€.")
  q = input("")
  os.system('clear')
  return MG_DM_linha_branca_frio
  
#Grande Domesticos Side-by-Side - Débito Mensal
def MG_DM_linha_branca_side_b_side():
  print("\033[1;35;40mMG - 9108274 --> 5,99€")
  print("\033[1;37;40mCoberturas:\n")
  print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias não cobertas pelo fabricante:\n    - Uso.\n    - Desgaste.\n    - Avarias provocadas pelo calcário.\n    Benefícios VIP:\n    - Três avarias iguais no período de doze meses,substituição do equipamento.\n    - Perda de alimentos refrigerados/congelados até 100€ por avaria.\n    - Reinstalação por mudança.\n    - Compromisso em tempo de reparação -> se não tiver o seu equipamento\n      reparado em menos de 10 dias úteis, será compensado com 100€.")
  q = input("")
  os.system('clear')
  return MG_DM_linha_branca_side_b_side
  
#Grandes Domesticos, equip. de queima - Débito Mensal
def MG_DM_linha_branca_queima():
  print("\033[1;35;40mMG - 9108275 --> 2,99€")
  print("\033[1;37;40mCoberturas:\n")
  print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias não cobertas pelo fabricante:\n    - Uso.\n    - Desgaste.\n    Beneficios VIP:\n    - Três avarias iguais no período de doze meses,substituição do equipamento.\n    - Reinstalação por mudança.\n    - Compromisso em tempo de reparação -> se não tiver o seu equipamento\n      reparado em menos de 10 dias úteis, será compensado com 100€.")
  q = input("")
  os.system('clear')
  return MG_DM_linha_branca_queima
  
#Tablets - débito mensal
def MG_DM_tablets():
  val = float(input("Introduza o valor do equipamento : "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 300:
    print("\033[1;35;40mMG - 9108276 --> 3,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 500:
    print("\033[1;35;40mMG - 9108277 --> 4,49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 800:
    print("\033[1;35;40mMG - 9108278 --> 5,49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 1200:
    print("\033[1;35;40mMG - 9108279 --> 6,49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 1800:
    print("\033[1;35;40mMG - 9108280 --> 8,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108281 --> 11,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 5000:
    print("\033[1;35;40mMG - 9108282 --> 14,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val > 5000:
    print("Só válido para equipamentos até 5000€")
    q = input("")
    os.system('clear')
  return MG_DM_tablets
  
#Informatica Portatil - Débito Mensal
def MG_DM_pc_portat():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108283 --> 3,49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no periodo de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108284 --> 3,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no periodo de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 800:
    print("\033[1;35;40mMG - 9108285 --> 5,49")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no periodo de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 1200:
    print("\033[1;35;40mMG - 9108286 --> 6,49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no periodo de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 1800:
    print("\033[1;35;40mMG - 9108287 --> 8,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no periodo de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108288 --> 10,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no periodo de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 5000:
    print("\033[1;35;40mMG - 9108289 --> 15,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no periodo de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val > 5000:
    print("Só válido para equipamentos até 5000€")
    q = input("")
    os.system('clear')
  return MG_DM_pc_portat
  
#Informatica Pro, portatil e não portatil - Débito Mensal
def MG_DM_informatica_pro():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 300:
    print("\033[1;35;40mMG - 9108193 --> 8,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Mau funcionamento, avaria ou dano acidental.")
    print("    Assistência Informática remota e telefónica.")
    print("    Equipamento de substituição temporária.")
    print("    Localização do equipamento (Roubo/Furto)")
    print("    Roubo ou Furto.")
    print("    Serviço de recuperação de dados.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108194 --> 9,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Mau funcionamento, avaria ou dano acidental.")
    print("    Assistência Informática remota e telefónica.")
    print("    Equipamento de substituição temporária.")
    print("    Localização do equipamento (Roubo/Furto)")
    print("    Roubo ou Furto.")
    print("    Serviço de recuperação de dados.")
    q = input("")
    os.system('clear')
  elif val <= 900:
    print("\033[1;35;40mMG - 9108195 --> 10,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Mau funcionamento, avaria ou dano acidental.")
    print("    Assistência Informática remota e telefónica.")
    print("    Equipamento de substituição temporária.")
    print("    Localização do equipamento (Roubo/Furto)")
    print("    Roubo ou Furto.")
    print("    Serviço de recuperação de dados.")
    q = input("")
    os.system('clear')
  elif val <= 1500:
    print("\033[1;35;40mMG - 9108196 --> 12,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Mau funcionamento, avaria ou dano acidental.")
    print("    Assistência Informática remota e telefónica.")
    print("    Equipamento de substituição temporária.")
    print("    Localização do equipamento (Roubo/Furto)")
    print("    Roubo ou Furto.")
    print("    Serviço de recuperação de dados.")
    q = input("")
    os.system('clear')
  elif val > 1500:
    print("Só válido para equipamentos até 1500€")
    q = input("")
    os.system('clear')
  return MG_DM_informatica_pro
  
#Informatica não portatil - Débito Mensal  
def MG_DM_informatica_n_portatil():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108297 --> 2,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no periodo de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 700:
    print("\033[1;35;40mMG - 9108298 --> 3,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no periodo de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 1000:
    print("\033[1;35;40mMG - 9108299 --> 4,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no periodo de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 1800:
    print("\033[1;35;40mMG - 9108300 --> 6,49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no periodo de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108301 --> 9,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no periodo de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val > 2500:
    print("Só válido para equipamentos até 2500€")
    q = input("")
    os.system('clear')
  return MG_DM_informatica_n_portatil

#Image e som não portatil - Débito Mensal  
def MG_DM_televisao():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108290 --> 2,49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.\n    - Reinstalação do equipamento seguro em caso de mudança.")
    q = input("")
    os.system('clear')
  elif val <= 600:
    print("\033[1;35;40mMG - 9108291 --> 2,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.\n    - Reinstalação do equipamento seguro em caso de mudança.")
    q = input("")
    os.system('clear')
  elif val <= 800:
    print("\033[1;35;40mMG - 9108292 --> 3,49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.\n    - Reinstalação do equipamento seguro em caso de mudança.")
    q = input("")
    os.system('clear')
  elif val <= 1200:
    print("\033[1;35;40mMG - 9108293 --> 4,49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.\n    - Reinstalação do equipamento seguro em caso de mudança.")
    q = input("")
    os.system('clear')
  elif val <= 1800:
    print("\033[1;35;40mMG - 9108294 --> 5,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.\n    - Reinstalação do equipamento seguro em caso de mudança.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108295 --> 7,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.\n    - Reinstalação do equipamento seguro em caso de mudança.")
    q = input("")
    os.system('clear')
  elif val <= 5000:
    print("\033[1;35;40mMG - 9108296 --> 9,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.\n    - Reinstalação do equipamento seguro em caso de mudança.")
    q = input("")
    os.system('clear')
  elif val > 5000:
    print("Só válido para equipamentos até 2500€")
    q = input("")
    os.system('clear')
  return MG_DM_televisao

#Fotografia - Débito Mensal
def MG_DM_fotografia():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108297 --> 2,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.\n")
    q = input("")
    os.system('clear')
  elif val <= 700:
    print("\033[1;35;40mMG - 9108298 --> 3,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.\n")
    q = input("")
    os.system('clear')
  elif val <= 1000:
    print("\033[1;35;40mMG - 9108299 --> 4,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.\n")
    q = input("")
    os.system('clear')
  elif val <= 1800:
    print("\033[1;35;40mMG - 9108300 --> 6,49€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.\n")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108301 --> 9,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.\n")
    q = input("")
    os.system('clear')
  elif val > 2500:
    print("Só válido para equipamentos até 2500€")
    q = input("")
    os.system('clear')
  return MG_DM_fotografia
  
#Entertenimento\Consolas - Débito Mensal  
def MG_DM_consolas():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108302 --> 3,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 700:
    print("\033[1;35;40mMG - 9108303 --> 5,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 1000:
    print("\033[1;35;40mMG - 9108304 --> 7,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 1800:
    print("\033[1;35;40mMG - 9108305 --> 9,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108306 --> 12,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val > 2500:
    print("Só válido para equipamentos até 2500€")
    q = input("")
    os.system('clear')
  return MG_DM_consolas
  
  
def MG_DM_imagem_e_som():
  val = float(input("Introduza o valor do equipamento: "))
  if val <= 0:
    print("Valor tem de ser maior que zero.")
    q = input("")
    os.system('clear')
  elif val <= 400:
    print("\033[1;35;40mMG - 9108307 --> 4,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 700:
    print("\033[1;35;40mMG - 9108308 --> 6,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 1000:
    print("\033[1;35;40mMG - 9108309 --> 8,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 1800:
    print("\033[1;35;40mMG - 9108310 --> 11,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val <= 2500:
    print("\033[1;35;40mMG - 9108311 --> 13,99€")
    print("\033[1;37;40mCoberturas:\n")
    print("    Avarias elétricas ou mecânicas.\n    Dano Acidental.\n    Avarias por uso e desgaste.\n    Furto qualificado.\n    Benefícios Adicionais:\n    - Três avarias iguais no período de 12 meses - substituição do equipamento.")
    q = input("")
    os.system('clear')
  elif val > 2500:
    print("Só válido para equipamentos até 2500€")
    q = input("")
    os.system('clear')
    ch = None
  return MG_DM_imagem_e_som


def SI_Encastre():
  os.system('clear')
  print("\033[1;37;45mEquipamentos de Encastre")
  print("\033[1;37;40m01 - \033[1;35;40m6800484 \033[1;37;40m- Instalação Placa Gás - \033[1;35;40m64,90€\033[1;37;40m")
  print("02 - \033[1;35;40m6800483 \033[1;37;40m- Instalação Placa Elétrica - \033[1;35;40m39,90€\033[1;37;40m")
  print("03 - \033[1;35;40m6800545 \033[1;37;40m- Instalação Placa Mista - \033[1;35;40m59,90€\033[1;37;40m")
  print("04 - \033[1;35;40m6800546 \033[1;37;40m- Instalação Placa Dominó Eletrica - \033[1;35;40m39,90€\033[1;37;40m")
  print("05 - \033[1;35;40m6800547 \033[1;37;40m- Instalação Placa Dominó Gás - \033[1;35;40m59,90€\033[1;37;40m")
  print("06 - \033[1;35;40m6800476 \033[1;37;40m- Instalação Forno Gás - \033[1;35;40m64,90€\033[1;37;40m")
  print("07 - \033[1;35;40m6800485 \033[1;37;40m- Instalação Forno Elétrico - \033[1;35;40m39,90€\033[1;37;40m")
  print("08 - \033[1;35;40m6800548 \033[1;37;40m- Instalação Forno Vapor - \033[1;35;40m64,90€\033[1;37;40m")
  print("09 - \033[1;35;40m6800486 \033[1;37;40m- Instalação Fogão Elétrico - \033[1;35;40m34,90€\033[1;37;40m")
  print("10 - \033[1;35;40m6800549 \033[1;37;40m- Instalação Fogão Misto - \033[1;35;40m34,90€\033[1;37;40m")
  print("11 - \033[1;35;40m6800491 \033[1;37;40m- Instalação Exaustor Gaveta e Parede - \033[1;35;40m54,90€\033[1;37;40m")
  print("12 - \033[1;35;40m6800225 \033[1;37;40m- Instalação Exaustor Ilhas e Teto - \033[1;35;40m79,90€\033[1;37;40m")
  print("13 - \033[1;35;40m6800492 \033[1;37;40m- Instalação Exaustor Chaminé - \033[1;35;40m54,90€\033[1;37;40m")
  print("14 - \033[1;35;40m6800493 \033[1;37;40m- Instalação Placa Gás + Forno Gás - \033[1;35;40m99,90€\033[1;37;40m")
  print("15 - \033[1;35;40m6800494 \033[1;37;40m- Instalação Placa Eletrica + Forno Elétrico - \033[1;35;40m49,90€\033[1;37;40m")
  print("16 - \033[1;35;40m6800495 \033[1;37;40m- Instalação Placa Gás + Forno Elétrico - \033[1;35;40m64,90€\033[1;37;40m")
  print("17 - \033[1;35;40m6800496 \033[1;37;40m- Instalação Placa Elétrica + Forno Gás - \033[1;35;40m64,90€\033[1;37;40m")
  print("18 - \033[1;35;40m6800497 \033[1;37;40m- Instalação Fogão Gás - \033[1;35;40m34,90€\033[1;37;40m")
  print("19 - \033[1;35;40m6800498 \033[1;37;40m- Instalação Encastre Maq. Lavar Roupa - \033[1;35;40m54,90€\033[1;37;40m")
  print("20 - \033[1;35;40m6800507 \033[1;37;40m- Instalação Encastre Maq. Lavar Louça - \033[1;35;40m54,90€\033[1;37;40m")
  print("\nEnter para avançar ... ")
  q = input("")
  os.system('clear')
  print("21 - \033[1;35;40m6800550 \033[1;37;40m- Instalação Encastre Maq. Secar Roupa - \033[1;35;40m54,90€\033[1;37;40m")
  print("22 - \033[1;35;40m6800551 \033[1;37;40m- Instalação Encastre Maq. Lavar e Secar Roupa - \033[1;35;40m54,90€\033[1;37;40m")
  print("23 - \033[1;35;40m6800499 \033[1;37;40m- Instalação Encastre Frigorifico - \033[1;35;40m54,90€\033[1;37;40m")
  print("24 - \033[1;35;40m6800508 \033[1;37;40m- Instalação Encastre Combinado - \033[1;35;40m54,90€\033[1;37;40m")
  print("25 - \033[1;35;40m6800500 \033[1;37;40m- Instalação Encastre Grandes Domésticos - \033[1;35;40m54,90€\033[1;37;40m")
  print("26 - \033[1;35;40m6800479 \033[1;37;40m- Serviço Instalação Deslocação Adicional - \033[1;35;40m30€\033[1;37;40m")
  print("27 - \033[1;35;40m6800502 \033[1;37;40m- Instalação Encastre Maq. Café - \033[1;35;40m44,90€\033[1;37;40m")
  print("28 - \033[1;35;40m6800475 \033[1;37;40m- Instalação Encastre Micro Ondas - \033[1;35;40m44,90€\033[1;37;40m")
  print("29 - \033[1;35;40m6800503 \033[1;37;40m- Instalação Emissores Térmicos - \033[1;35;40m40€\033[1;37;40m")
  print("30 - \033[1;35;40m6800556 \033[1;37;40m- Instalação Placa Dominó Elétrica + Forno Eletrico - \033[1;35;40m49,90€\033[1;37;40m")
  print("31 - \033[1;35;40m6800557 \033[1;37;40m- Instalação Placa Dominó Elétrica + Forno Gas - \033[1;35;40m64,90€\033[1;37;40m")
  print("32 - \033[1;35;40m6800558 \033[1;37;40m- Instalação Placa Dominó Elétrica + Forno Vapor - \033[1;35;40m64,90€\033[1;37;40m")
  print("33 - \033[1;35;40m6800559 \033[1;37;40m- Instalação Placa Dominó Gás + Forno Eletrico - \033[1;35;40m64,90€\033[1;37;40m")
  print("34 - \033[1;35;40m6800560 \033[1;37;40m- Instalação Placa Dominó Gás + Forno Gas - \033[1;35;40m99,90€\033[1;37;40m")
  print("35 - \033[1;35;40m6800561 \033[1;37;40m- Instalação Placa Dominó Gás + Forno Vapor - \033[1;35;40m99,90€\033[1;37;40m")
  print("36 - \033[1;35;40m6800562 \033[1;37;40m- Instalação Placa Elétrica + Forno Vapor - \033[1;35;40m64,90€\033[1;37;40m")
  print("37 - \033[1;35;40m6800563 \033[1;37;40m- Instalação Placa Gás + Forno Vapor - \033[1;35;40m99,90€\033[1;37;40m")
  print("38 - \033[1;35;40m6800564 \033[1;37;40m- Instalação Placa Mista + Forno Elétrico - \033[1;35;40m64,90€\033[1;37;40m")
  print("39 - \033[1;35;40m6800565 \033[1;37;40m- Instalação Placa Mista + Forno Gás - \033[1;35;40m99,90€\033[1;37;40m")
  print("40 - \033[1;35;40m6800566 \033[1;37;40m- Instalação Placa Mista + Forno Vapor - \033[1;35;40m99,90€\033[1;37;40m")
  print("41 - \033[1;35;40m6800514 \033[1;37;40m- Instalação Placa Gás com remoção Antiga - \033[1;35;40m69,90€\033[1;37;40m")
  print("\nEnter para sair ...")
  

def SI_Esq_e_Cald():
  os.system('clear')
  print("\033[1;37;45mEsquentadores e Caldeiras")
  print("\033[1;37;40m01 - \033[1;35;40m6800487\033[1;37;40m - Instalação Esquentador Gás Natural - \033[1;35;40m64,90€ ")
  print("\033[1;37;40m02 - \033[1;35;40m6800552\033[1;37;40m - Instalação Esquentador Gás Butano - \033[1;35;40m64,90€")
  print("\033[1;37;40m03 - \033[1;35;40m6800553\033[1;37;40m - Instalação Esquentador Elétrico - \033[1;35;40m64,90€")
  print("\033[1;37;40m04 - \033[1;35;40m6800488\033[1;37;40m - Instalação Esquentador - Express 24h - \033[1;35;40m79,90€")
  print("\033[1;37;40m05 - \033[1;35;40m6800479\033[1;37;40m - Serviço Instalação Deslocação Adicional - \033[1;35;40m25€")
  print("\033[1;37;40m06 - \033[1;35;40m6800515\033[1;37;40m - Instalação Esquentador c/Remoção Antigo - \033[1;35;40m69,90€")
  print("\033[1;37;40m07 - \033[1;35;40m6800577\033[1;37;40m - Instalação Caldeira Mural a Gás - \033[1;35;40m189,90€")
  print("\033[1;37;40m08 - \033[1;35;40m6800578\033[1;37;40m - Instalação Caldeira Mural a Gasóleo - \033[1;35;40m239,90€")
  print("\033[1;37;40m09 - \033[1;35;40m6800579\033[1;37;40m - Remoção Caldeira Antiga - \033[1;35;40m30€")
  print("\n\033[1;37;40mEnter para sair ...")
  
  
def SI_Termoac():
  os.system('clear')
  print("\033[1;37;45mTermoacomuladores")
  print("\033[1;37;40m01 - \033[1;35;40m6800489\033[1;37;40m - Instalação Cilindro Elétrico ate 50L - \033[1;35;40m49,90€")
  print("\033[1;37;40m02 - \033[1;35;40m6800490\033[1;37;40m - Instalaçao Cilindro Elétrico > 50L - \033[1;35;40m69,90€")
  print("\033[1;37;40m03 - \033[1;35;40m6800479\033[1;37;40m - Serviço Instalação Deslocação Adicional - \033[1;35;40m25€")
  print("\n\033[1;37;40mEnter para sair ...")

  
def SI_Serv_Suplem():
  os.system('clear')
  print("\033[1;37;45mServiços Suplementares")
  print("\033[1;37;40m01 - \033[1;35;40m6800504\033[1;37;40m - Inversão sentido das portas - \033[1;35;40m39,90€")
  print("\033[1;37;40m02 - \033[1;35;40m6800506\033[1;37;40m - Contrato Manutenção Equipamentos Gás - \033[1;35;40m84,90€")
  print("\033[1;37;40m03 - \033[1;35;40m6800480\033[1;37;40m - Taxa Noturna das 18h as 22h - \033[1;35;40m37,50€")
  print("\033[1;37;40m04 - \033[1;35;40m6800478\033[1;37;40m - Taxa Adicional Sábado das 8h as 18h - \033[1;35;40m37,50€")
  print("\033[1;37;40m05 - \033[1;35;40m6800481\033[1;37;40m - Taxa Adicional Domingo das 8h as 18h - \033[1;35;40m42,50€")
  print("\033[1;37;40m06 - \033[1;35;40m6800477\033[1;37;40m - Taxa Adicional Feriado das 8h as 18h - \033[1;35;40m42,50€")
  print("\033[1;37;40m07 - \033[1;35;40m6800509\033[1;37;40m - Troca injetores fogões s/Instalação - \033[1;35;40m39,90€")
  print("\033[1;37;40m08 - \033[1;35;40m6800510\033[1;37;40m - Troca injetores fogões c/Instalação - \033[1;35;40m19,90€")
  print("\033[1;37;40m09 - \033[1;35;40m6800511\033[1;37;40m - Instalação de Triturador - \033[1;35;40m34,90€")
  print("\033[1;37;40m10 - \033[1;35;40m6800505\033[1;37;40m - Remoção 1 Equipamento Antigo c/Instalação - \033[1;35;40m12,50€")
  print("\033[1;37;40m11 - \033[1;35;40m6800567\033[1;37;40m - Remoção 2 Equipamentos Antigos c/Instalação - \033[1;35;40m20€")
  print("\033[1;37;40m12 - \033[1;35;40m6800569\033[1;37;40m - Remoção 3 Equipamentos Antigos c/Instalação - \033[1;35;40m30€")
  print("\033[1;37;40m13 - \033[1;35;40m6800570\033[1;37;40m - Remoção 1 Equipamento Antigo s/Instalação - \033[1;35;40m35€")
  print("\033[1;37;40m14 - \033[1;35;40m6800571\033[1;37;40m - Remoção 2 Equipamentos Antigos s/Instalação - \033[1;35;40m45€")
  print("\033[1;37;40m15 - \033[1;35;40m6800572\033[1;37;40m - Remoção 3 Equipamentos Antigos s/Instalação - \033[1;35;40m55€")
  print("\033[1;37;40m16 - \033[1;35;40m6800512\033[1;37;40m - Serviço de Orçamentação - \033[1;35;40m30€\033[1;37;40m")
  print("\nEnter para sair ...")



def exit_program():
  quit()


c = None
while c is None:
  try:
    print("          \033[1;35;40m ___  ___                        ")
    print("          | . \| . \                       ")
    print("          |   /|  _/                       ")
    print("          |_\_\|_|                         ")                                           
    print("\033[0;36;40m")
    
    w = "::::::::(RP-TOOLKIT):::::::::"
    for char in w:
      sleep(0.03)
      sys.stdout.write(char)
      sys.stdout.flush()
      
    print("\n")
    print("\033[1;35;40m1 - \033[1;37;40mRP Megas")
    print("\033[1;35;40m2 - \033[1;37;40mRP Instalações")
    print("\033[1;35;40m3 - \033[1;37;40mRP Transportes Viatura 60")
    print("\033[1;35;40m4 - \033[1;37;40mContactos de Lojas")
    print("\033[1;35;40m5 - \033[1;37;40mAcerca deste script")
    print("\033[1;35;40m6 - \033[1;37;40mSair\n")
    
    c = int(input(""))
    os.system('clear') 
    if c == 1:
      ch = None 
      while ch is None:
        try:
          print("\033[1;35;40mRP - MEGAS GARANTIAS\n\n")
          print("\033[1;35;40m01 - \033[1;37;40mGrandes Domésticos\n\033[1;35;40m02 - \033[1;37;40mPequenos Domésticos\n\033[1;35;40m03 - \033[1;37;40mInformática Portátil\n\033[1;35;40m04 - \033[1;37;40mInformática Não Portátil\n\033[1;35;40m05 - \033[1;37;40mImagem e Som Não Portátil\n\033[1;35;40m06 - \033[1;37;40mImagem e Som Portátil\n\033[1;35;40m07 - \033[1;37;40mTelemóveis\n\033[1;35;40m08 - \033[1;37;40mFotografia\n\033[1;35;40m09 - \033[1;37;40mConsolas e Jogos\n\033[1;35;40m10 - \033[1;37;40mSmartwatch\n\033[1;35;40m11 - \033[1;37;40mRetroceder\n\033[1;35;40m12 - \033[1;37;40mSair\n")
          ch = int(input(""))
          os.system('clear')
          if ch == 1:
            print("\033[1;37;45m01 - GRANDES DOMÉSTICOS\n")
            print("\033[1;35;40m1 - \033[1;37;40mMG - Ampliar para 5 anos")
            print("\033[1;35;40m2 - \033[1;37;40mMG - Ampliar para 3 anos")
            print("\033[1;35;40m3 - \033[1;37;40mMG - Débito Mensal - Linha Branca Frio")
            print("\033[1;35;40m4 - \033[1;37;40mMG - Débito Mensal - Linha Branca Side by Side")
            print("\033[1;35;40m5 - \033[1;37;40mMG - Débito Mensal - Linha Branca Queima/MLR/MLL/MSR/Exaustor/Microondas")
            print("\033[1;35;40m6 - \033[1;37;40mMG - Débito Direto - Cozinha Completa")
            print("\033[1;35;40m7 - \033[1;37;40mMG - Débito Direto - Ar Condicionado\n")
            option = int(input(""))
            os.system('clear')

            if option == 1:
              print("\033[1;37;45mAmpliar para 5 anos\033[1;37;40m")
              MG_electrodomesticos_5_anos()
              ch = None
            elif option == 2:
              print("\033[1;37;45mAmpliar para 3 anos\033[1;37;40m")
              MG_electrodomesticos_3_anos()
              ch = None
            elif option == 3:
              print("\033[1;37;45mDébito Mensal - Linha Branca Frio\033[1;37;40m")
              MG_DM_linha_branca_frio()
              ch = None
            elif option == 4:
              print("\033[1;37;45mDébito Mensal - Linha Branca Side by Side\033[1;37;40m")
              MG_DM_linha_branca_side_b_side()
              ch = None
            elif option == 5:
              print("\033[1;37;45mDébito Mensal - Linha Branca Queima/MLR/MLL/MSR/Exaustor/Microondas\033[1;37;40m")
              MG_DM_linha_branca_queima()
              ch = None
            elif option == 6:
              MG_eletrodomesticos_deb_direto_cozinha_completa()
              ch = None
            elif option == 7:
              MG_eletrodomesticos_deb_direto_ar_condicionado()
              ch = None
            else:
              os.system('clear')
              ch = None
          elif ch == 2:
            print("\033[1;37;45m02 - PEQUENOS DOMÉSTICOS\n")
            print("\033[1;35;40m1 - \033[1;37;40mMG - Troca Direta 1 Ano")
            print("\033[1;35;40m2 - \033[1;37;40mMG - Ampliar Garantia para 3 Anos")
            option = int(input(""))
            if option == 1:
              os.system('clear')
              print("\033[1;37;45mTroca Direta 1 Ano\033[1;37;40m")
              MG_troca_direta_peq_dom_1_ano()
              ch = None
            elif option == 2:
              os.system('clear')
              print("\033[1;37;45mAmpliar Garantia para 3 Anos\033[1;37;40m")
              MG_electrodomesticos_3_anos()
              ch = None
            else:
              os.system('clear')
              ch = None
          elif ch == 3:
            print("\033[1;37;45m03 - INFORMATICA PORTATIL\n")
            print("\033[1;35;40m01 -\033[1;37;40m MG - Ampliar Garantia para 5 Anos")
            print("\033[1;35;40m02 -\033[1;37;40m MG - Proteção Total 3 Anos ")
            print("\033[1;35;40m03 -\033[1;37;40m MG - Danos Acidentais 1 Ano")
            print("\033[1;35;40m04 -\033[1;37;40m MG - TABLETS - Proteção Quebra de Ecra 2 Anos")
            print("\033[1;35;40m05 -\033[1;37;40m MG - EBOOKS - Proteção Quebra de Ecra 2 Anos")
            print("\033[1;35;40m06 -\033[1;37;40m MG - DISCOS EXTERNOS - Danos Acidentais 2 Anos")
            print("\033[1;35;40m07 -\033[1;37;40m MG - SPV 1 Ano")
            print("\033[1;35;40m08 -\033[1;37;40m MG - Informática Pro Débito Direto")
            print("\033[1;35;40m09 -\033[1;37;40m MG - Débito Mensal - Computadores Portáteis")
            print("\033[1;35;40m10 -\033[1;37;40m MG - Débito Mensal - Tablets")
            print("\033[1;35;40m11 -\033[1;37;40m MG - Débito Mensal - Informática Pro\n")
            option = int(input(""))
            os.system('clear')
            if option == 1:
              print("\033[1;37;45mAmpliar Garantia para 5 Anos\033[1;37;40m")
              MG_informatica_5_anos_portatil()
              ch = None
            elif option == 2:
              print("\033[1;37;45mProteção Total 3 Anos\033[1;37;40m")
              MG_informatica_portatil_protecao_total_3_anos()
              ch = None
            elif option == 3:
              print("\033[1;37;45mDanos Acidentais 1 Ano\033[1;37;40m")
              MG_informatica_danos_acidentais_1_ano()
              ch = None
            elif option == 4:
              print("\033[1;37;45mTABLETS - Proteção Quebra de Ecra 2 Anos\033[1;37;40m")
              MG_quebra_ecra_tablets_2_anos()
              ch = None
            elif option == 5:
              print("\033[1;37;45mEBOOKS - Proteção Quebra de Ecra 2 Anos\033[1;37;40m")
              MG_quebra_ecra_ebooks_2_anos()
              ch = None
            elif option == 6:
              print("\033[1;37;45mDISCOS EXTERNOS - Danos Acidentais 2 Anos\033[1;37;40m")
              MG_danos_acidentais_2_anos_discos_externos()
              ch = None
            elif option == 7:
              print("\033[1;37;45mSPV 1 Ano\033[1;37;40m")
              MG_informatica_spv_1_ano()
              ch = None
            elif option == 8:
              print("\033[1;37;45mInformática Pro Débito Direto\033[1;37;40m")
              MG_informatica_pro_debito_direto()
              ch = None
            elif option == 9:
              print("\033[1;37;45mDébito Mensal - Computadores Portáteis\033[1;37;40m")
              MG_DM_pc_portat()
              ch = None
            elif option == 10:
              print("\033[1;37;45mDébito Mensal - Tablets\033[1;37;40m")
              MG_DM_tablets()
              ch = None
            elif option == 11:
              print("\033[1;37;45mDébito Mensal - Informática Pro\033[1;37;40m")
              MG_DM_informatica_pro()
              ch = None
            else:
              os.system('clear')
              ch = None
          elif ch == 4:
            print("\033[1;37;45m04 - INFORMATICA NÃO PORTATIL\n")
            print("\033[1;35;40m1 -\033[1;37;40m MG - Ampliar Garantia para 5 Anos")
            print("\033[1;35;40m2 -\033[1;37;40m MG - Proteção Total 3 Anos")
            print("\033[1;35;40m3 -\033[1;37;40m MG - Danos Acidentais 1 Ano")
            print("\033[1;35;40m4 -\033[1;37;40m MG - Débito Mensal - Informática não Portátil")
            print("\033[1;35;40m5 -\033[1;37;40m MG - Débito Mensal - Informática Pro\n")
            option = int(input(""))
            os.system('clear')
            if option == 1:
              print("\033[1;37;45mAmpliar Garantia para 5 Anos\033[1;37;40m")
              MG_informatica_5_anos_n_portatil()
              ch = None
            elif option == 2:
              print("\033[1;37;45mProteção Total 3 Anos\033[1;37;40m")
              MG_informatica_n_portatil_protecao_total_3_anos()
              ch = None
            elif option == 3:
              print("\033[1;37;45mDanos Acidentais 1 Ano\033[1;37;40m")
              MG_informatica_danos_acidentais_1_ano()
              ch = None
            elif option == 4:
              print("\033[1;37;45mDébito Mensal - Informática não Portátil\033[1;37;40m")
              MG_DM_informatica_n_portatil()
              ch = None
            elif option == 5:
              print("\033[1;37;45mDébito Mensal - Informática Pro\033[1;37;40m")
              MG_DM_informatica_pro()    
              ch = None
            else:
              os.system('clear')
              ch = None
          elif ch == 5:
            print("\033[1;37;45m05 - IMAGEM E SOM NÃO PORTATIL\n")
            print("\033[1;35;40m1 -\033[1;37;40m MG - Ampliar Garantia para 5 Anos")
            print("\033[1;35;40m2 -\033[1;37;40m MG - Proteção Total 3 Anos")
            print("\033[1;35;40m3 -\033[1;37;40m MG - SPV 1 Ano")
            print("\033[1;35;40m4 -\033[1;37;40m MG - Troca Direta")
            print("\033[1;35;40m5 -\033[1;37;40m MG - Débito Mensal - Imagem e Som\n")
            option = int(input(""))
            os.system('clear')
            if option == 1:
              print("\033[1;37;45mAmpliar Garantia para 5 Anos\033[1;37;40m")
              MG_imagem_som_5_anos_n_portatil()
              ch = None
            elif option == 2:
              print("\033[1;37;45mProteção Total 3 Anos\033[1;37;40m")
              MG_imagem_som_3_anos_n_portatil()
              ch = None
            elif option == 3:
              print("\033[1;37;45mSPV 1 Ano\033[1;37;40m")
              MG_imagem_som_SPV_1_ano()
              ch = None
            elif option == 4:
              print("\033[1;37;45mTroca Direta\033[1;37;40m")
              MG_imagem_som_troca_direta()
              ch = None
            elif option == 5:
              print("\033[1;37;45mDébito Mensal - Imagem e Som\033[1;37;40m")
              MG_DM_televisao()    
              ch = None
            else:
              os.system('clear')
              ch = None
          elif ch == 6:
            print("\033[1;37;45m06 - IMAGEM E SOM PORTATIL\n")
            print("\033[1;35;40m1 -\033[1;37;40m MG - Proteção Total 3 Anos")
            print("\033[1;35;40m2 -\033[1;37;40m MG - SPV 1 Ano")
            print("\033[1;35;40m3 -\033[1;37;40m MG - Troca Direta")
            print("\033[1;35;40m4 -\033[1;37;40m MG - Débito Mensal - Imagem e Som (Excepto TV's)\n")
            option = int(input(""))
            os.system('clear')
            if option == 1:
              print("\033[1;37;45mProteção Total 3 Anos\033[1;37;40m")
              MG_imagem_som_3_anos_portatil()
              ch = None
            elif option == 2:
              print("\033[1;37;45mSPV 1 Ano\033[1;37;40m")
              MG_imagem_som_SPV_1_ano()
              ch = None
            elif option == 3:
              print("\033[1;37;45mTroca Direta\033[1;37;40m")
              MG_imagem_som_troca_direta()
              ch = None
            elif option == 4:
              print("\033[1;37;45mDébito Mensal - Imagem e Som (Excepto TV's)\033[1;37;40m")
              MG_DM_imagem_e_som()
              ch = None
            else:
              os.system('clear')
              ch = None
          elif ch == 7:
            print("\033[1;37;45m07 - TELEMÓVEIS\n")
            print("\033[1;35;40m1 -\033[1;37;40m MG - Proteção Quebra de Ecra 1 Ano")
            print("\033[1;35;40m2 -\033[1;37;40m MG - Plus 1 Ano")
            print("\033[1;35;40m3 -\033[1;37;40m MG - Plus Proteção Total Débito Direto\n")
            option = int(input(""))
            os.system('clear')
            if option == 1:
              print("\033[1;37;45mProteção Quebra de Ecra 1 Ano\033[1;37;40m")
              MG_telemoveis_quebra_ecra()
              ch = None
            elif option == 2:
              print("\033[1;37;45mPlus 1 Ano\033[1;37;40m")
              MG_telemoveis_plus()
              ch = None
            elif option == 3:
              print("\033[1;37;45mPlus Proteção Total Débito Direto\033[1;37;40m")
              MG_telemveis_plus_prot_total()
              ch = None
            else:
              os.system('clear')
              ch = None
          elif ch == 8:
            print("\033[1;37;45m08 - FOTOGRAFIA\n")
            print("\033[1;35;40m1 -\033[1;37;40m MG - Proteção Total 3 Anos")
            print("\033[1;35;40m2 -\033[1;37;40m MG - Proteção Total 1 Ano")
            print("\033[1;35;40m3 -\033[1;37;40m MG - SPV 1 Ano")
            print("\033[1;35;40m4 -\033[1;37;40m MG - Troca Direta 1 Ano")
            print("\033[1;35;40m5 -\033[1;37;40m MG - Débito Mensal - Fotografia\n")
            option = int(input(""))
            os.system('clear')
            if option == 1:
              print("\033[1;37;45mProteção Total 3 Anos\033[1;37;40m")
              MG_fotografia_prot_total_3_anos()
              ch = None
            elif option == 2:
              print("\033[1;37;45mProteção Total 1 Ano\033[1;37;40m")
              MG_fotografia_prot_total_1_ano()
              ch = None
            elif option == 3:
              print("\033[1;37;45mSPV 1 Ano\033[1;37;40m")
              MG_fotografia_spv_1_ano()
              ch = None
            elif option == 4:
              print("\033[1;37;45mTroca Direta 1 Ano\033[1;37;40m")
              MG_fotografia_troca_direta()
              ch = None
            elif option == 5:
              print("\033[1;37;45mDébito Mensal - Fotografia\033[1;37;40m")
              MG_DM_fotografia()
              ch = None
            else:
              os.system('clear')
              ch = None
          elif ch == 9:
            print("\033[1;37;45m09 - CONSOLAS E JOGOS\n")
            print("\033[1;35;40m1 -\033[1;37;40m MG - Proteção Total 3 Anos") 
            print("\033[1;35;40m2 -\033[1;37;40m MG - Troca Direta 3 Anos")
            print("\033[1;35;40m3 -\033[1;37;40m MG - Jogos Troca Direta 1 Ano")
            print("\033[1;35;40m4 -\033[1;37;40m MG - Débito Mensal - Consolas\n")
            option = int(input(""))
            os.system('clear')
            if option == 1:
              print("\033[1;37;45mProteção Total 3 Anos\033[1;37;40m")
              MG_entertenimento_prot_total_3_anos()
              ch = None
            elif option == 2:
              print("\033[1;37;45mTroca Direta 3 Anos\033[1;37;40m")
              MG_entertenimeto_troca_direta_3_anos()
              ch = None
            elif option == 3:
              print("\033[1;37;45mJogos Troca Direta 1 Ano\033[1;37;40m")
              MG_entertenimento_substituicao_direta_1_ano_jogos()
              ch = None
            elif option == 4:
              print("\033[1;37;45mDébito Mensal - Consolas\033[1;37;40m")
              MG_DM_consolas()
              ch = None
            else:
              os.system('clear')
              ch = None
          elif ch == 10:
            print("\033[1;37;45m10 - SMARTWATCH\n")
            print("\033[1;35;40m1 -\033[1;37;40m MG - Proteção Quebra de Ecra 1 Ano")
            print("\033[1;35;40m2 -\033[1;37;40m MG - Plus")
            print("\033[1;35;40m3 -\033[1;37;40m MG - Plus Proteção Total 1 Ano\n")
            option = int(input(""))
            os.system('clear')
            if option == 1:
              print("\033[1;37;45mProteção Quebra de Ecra 1 Ano\033[1;37;40m")
              MG_smartwatch_quebra_ecra()
              ch = None
            elif option == 2:
              print("\033[1;37;45mProteção Plus\033[1;37;40m")
              MG_smartwatch_plus()
              ch = None
            elif option == 3:
              print("\033[1;37;45mPlus Proteção Total 1 Ano\033[1;37;40m")
              MG_smartwatch_plus_prot_total()    
              ch = None
            else:
              os.system('clear')
              ch = None
          elif ch == 11:
            c = None
          elif ch == 12:
            exit_program()
          else:
            os.system('clear')
            ch = None
        except ValueError:
          print("")
          os.system('clear')
          ch = None      
    elif c == 2:
      print("\033[1;35;40mRP - SERVIÇOS DE INSTALAÇÃO\n\n")
      print("\033[1;35;40m1 - \033[1;37;40mEquipamentos de Encastre")
      print("\033[1;35;40m2 - \033[1;37;40mEsquentadores e Caldeiras")
      print("\033[1;35;40m3 - \033[1;37;40mTermoacumuladores")
      print("\033[1;35;40m4 - \033[1;37;40mServiços Suplementares\n")
      q = int(input(""))
      if q == 1:
        SI_Encastre()
        q = input("")
        os.system('clear')
        c = None
      elif q == 2:
        SI_Esq_e_Cald()
        q = input("")
        os.system('clear')
        c = None
      elif q == 3:
        SI_Termoac()
        q = input("")
        os.system('clear')
        c = None
      elif q == 4:
        SI_Serv_Suplem()
        q = input("")
        os.system('clear')
        c = None
      else:
        os.system('clear')
        c = None
    elif c == 3:
      print("\033[1;35;40mRP - NORMAS DE UTILIZAÇÃO DA VIATURA 60\n\n")
      print("\033[1;35;40m1 - \033[1;37;40mLojas Continente")
      print("\033[1;35;40m2 - \033[1;37;40mLojas São Miguel e Madeira\n")
      q = int(input(""))
      if q == 1:
        os.system('clear')
        print("\033[1;35;40mRP - NORMAS DE TRANSPORTE DE EQUIPAMENTOS VIATURA 60 - \033[1;37;45mLojas do Continente")
        print("\033[0;37;40m\n--------------------------------------------------------------------------------")
        print("\033[0;37;40m|\033[0;36;40mArmazém Venda\033[0;37;40m|\033[0;36;40mProdutos pequeno porte\033[1;37;40m*\033[0;36;40m(até 30kg)\033[0;37;40m|\033[0;36;40mProdutos grande porte (+30kg)\033[0;37;40m |")
        print("\033[0;37;40m|      -      |\033[0;36;40m Produtos Tecnologia PVP > 199€  \033[0;37;40m|                              |")
        print("|\033[0;36;40mArmazém Saida\033[0;37;40m|\033[0;36;40m  Restantes Produtos PVP > 99€   \033[0;37;40m|\033[0;36;40m    Transferência Interna\033[0;37;40m     |")
        print("\033[0;37;40m--------------------------------------------------------------------------------")
        print("\033[0;37;40m|\033[0;37;40m Loja(venda) \033[0;37;40m|                                 | Não é possivel (só situações |")
        print("\033[0;37;40m|\033[0;37;40m     p/      \033[0;37;40m|         CTT Expresso            |    de exceção previamente    |")
        print("\033[0;37;40m|\033[0;37;40m Loja(saida) \033[0;37;40m|                                 |      validadas pelo DO)      |")
        print("\033[0;37;40m--------------------------------------------------------------------------------")  
        print("\033[0;37;40m| Loja(Venda) |   Carros transferências (se     |                              |")
        print("\033[0;37;40m|     p/      | demorar no máx. 48h a chegar à  |        Transferência         |")
        print("\033[0;37;40m|Arm. Central | loja),se demorar mais utilizar  |         Prioritária          |")
        print("\033[0;37;40m|   (saida)   |         CTT Expresso            |                              |")
        print("\033[0;37;40m--------------------------------------------------------------------------------")
        print('\033[0;37;40m|\033[1;37;40m*\033[0;36;40mnão inclui TV >= 32"\033[0;37;40m                                                         |')
        print("\033[0;37;40m--------------------------------------------------------------------------------")
        print('\033[0;37;40m|\033[1;37;40mNota:\033[0;36;40mA loja da Terceira não pode vender de outras lojas nem do armazém central\033[0;37;40m|')
        print("\033[0;37;40m--------------------------------------------------------------------------------")
        print("\n\n")
        q = input("")
        os.system('clear')
        c = None
      elif q == 2:
        os.system('clear')
        print("\033[1;35;40mRP - NORMAS DE TRANSPORTE DE EQUIPAMENTOS VIATURA 60 - \033[1;37;45mLojas de S.Miguel/Madeira")
        print("\033[0;37;40m\n--------------------------------------------------------------------------------")
        print("\033[0;37;40m|\033[0;36;40mArmazém Venda\033[0;37;40m|\033[0;36;40mProdutos pequeno porte\033[1;37;40m*\033[0;36;40m(até 10kg)\033[0;37;40m|\033[0;36;40m       Produtos + 10kg       \033[0;37;40m |")
        print("\033[0;37;40m|      -      |\033[0;36;40m Produtos Tecnologia PVP > 399€  \033[0;37;40m|                              |")
        print("|\033[0;36;40mArmazém Saida\033[0;37;40m|\033[0;36;40m  Restantes Produtos PVP > 199€  \033[0;37;40m|\033[0;36;40m    Transferência Interna\033[0;37;40m     |")
        print("\033[0;37;40m--------------------------------------------------------------------------------")
        print("\033[0;37;40m|\033[0;37;40m Loja(venda) \033[0;37;40m|                                 | Não é possivel (só situações |")
        print("\033[0;37;40m|\033[0;37;40m     p/      \033[0;37;40m|         CTT Expresso            |    de exceção previamente    |")
        print("\033[0;37;40m|\033[0;37;40m Loja(saida) \033[0;37;40m|                                 |      validadas pelo DO)      |")
        print("\033[0;37;40m--------------------------------------------------------------------------------")  
        print("\033[0;37;40m| Loja(Venda) |                                 |                              |")
        print("\033[0;37;40m|     p/      |         CTT Expresso            |        Transferência         |")
        print("\033[0;37;40m|Arm. Central |                                 |         Prioritária          |")
        print("\033[0;37;40m|   (saida)   |                                 |                              |")
        print("\033[0;37;40m--------------------------------------------------------------------------------")
        print('\033[0;37;40m|\033[1;37;40m*\033[0;36;40mnão inclui TV >= 32"\033[0;37;40m                                                         |')
        print("\033[0;37;40m--------------------------------------------------------------------------------")
        print('\033[0;37;40m|\033[1;37;40mNota:\033[0;36;40mA loja da Terceira não pode vender de outras lojas nem do armazém central\033[0;37;40m|')
        print("\033[0;37;40m--------------------------------------------------------------------------------")
        print("\n\n")
        q = input("")
        os.system('clear')
        c = None
      else:
        os.system('clear')
        c = None
    elif c == 4:
      print("\033[1;35;40mRP - CONTACTOS DE LOJAS RP\n\n")
      print("\033[1;35;40m01 - \033[1;37;40mServiços Centrais")
      print("\033[1;35;40m02 - \033[1;37;40mZona Norte")
      print("\033[1;35;40m03 - \033[1;37;40mGrande Porto")
      print("\033[1;35;40m04 - \033[1;37;40mZona Centro")
      print("\033[1;35;40m05 - \033[1;37;40mGrande Lisboa")
      print("\033[1;35;40m06 - \033[1;37;40mZona Sul")
      print("\033[1;35;40m07 - \033[1;37;40mIlhas\n")
      q = int(input(""))
      os.system('clear')
      if q == 1:
        print("\033[1;37;45mRP - Serviços Centrais(Enter->Sair)\n")
        print("\033[1;35;40mRP - SEDE\033[1;37;40m\t\t\t\t\033[1;35;40mRP - ARMAZEM CENTRAL\033[1;37;40m")
        print("Aguda Parque\t\t\t\tAguda Parque")
        print("Largo de Arcozelo,nº 76-Edificio E\tLargo de Arcozelo,nº 76-Cais 27")
        print("4410-455 Arcozelo - V.N. Gaia\t\t4410-455 Arcozelo - V.N. Gaia")
        print("Ext: 7011\t\t\t\tExt: 4609-4615")
        print("\t\t\t\t\tCódigo SA-004 | SAP - 1000\n\n") # --------------------------------------------------
        print("\033[1;35;40mRP - TIC\033[1;37;40m\t\t\t\t\033[1;35;40mRP - SERVIÇO PÓS VENDA\033[1;37;40m")
        print("Estrada Nacional 14 (Km 7)\t\tAguda Parque")
        print("Lugar do Chiolo - Barca\t\t\tLargo de Arcozelo,nº 76-Cais 27")
        print("4475-045 Maia\t\t\t\t4410-455 Arcozelo - V.N. Gaia")
        print("Ext: 7209\n\n\n\n\n\n\n\n") # ------------------------------------------------------------------------------
        q = input("")
        os.system('clear')
        c = None
      elif q == 2:
        print("\033[1;37;45mRP - Zona Norte(Enter->Avançar)\n")
        print("\033[1;35;40mRP - BRAGA\033[1;37;40m\t\t\t\t\033[1;35;40mRP - VIANA DO CASTELO\033[1;37;40m")
        print("Braga Retail Center\t\t\tViana Retail Center")
        print("Quinta de Passos, S. Vitor - Loja J\tAv. da Estação, 584 - Loja B")
        print("4710-426 Braga\t\t\t\t4935-238 Viana do Castelo")
        print("Ext: 3901-3908\t\t\t\tExt: 2401-2408")
        print("Código SA-276 | SAP - 1144\t\tCódigo SA-121 | SAP - 1124\n")
        print("\033[1;35;40mRP - FAMALICÃO\033[1;37;40m\t\t\t\t\033[1;35;40mRP - VILA REAL\033[1;37;40m")
        print("Atlantic Park Famalicão\t\t\tEdificio Nervir")
        print("Estrada Nacional 204 - Loja 9\t\tAlameda de Grasse")
        print("4770-282 V.N. Famalicão\t\t\t5000-703 Vila Real")
        print("Ext: 4201-4208\t\t\t\tExt: 4101-4108")
        print("Código SA-080 | SAP - 1116\t\tCódigo SA-075 | SAP - 1115\n")
        print("\033[1;35;40mRP - GUIMARÃES\033[1;37;40m\t\t\t\t\033[1;35;40mRP - CHAVES\033[1;37;40m")
        print("R.São Miguel, nº653 - Creixomil\t\tRetail Park Chaves")
        print("4835-106 Guimarães\t\t\tAvenida D.João I - Nacional 13")
        print("Ext: 4301-4308\t\t\t\tRotunda do Raio X")
        print("Código SA-100 | SAP - 1117\t\t5400-323 Chaves")
        print("                          \t\tExt: 4501-4508")
        print("                          \t\tCódigo SA-292 | SAP - 1152")
        q = input("")
        os.system('clear')
        print("\033[1;37;45mRP - Zona Norte(Enter->Sair)\n")
        print("\033[1;35;40mRP - MONÇÃO\033[1;37;40m")
        print("Rio Park Monção")
        print("Rio Park, Loja A, Monte da Mina, Lodeira")
        print("4950-852 Cortes")
        print("Ext: 2501-2508")
        print("Código SA-286 | SAP - 1149\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        q = input("")
        os.system('clear')
        c = None
      elif q == 3:
        print("\033[1;37;45mRP - Grande Porto(Enter->Avançar)\n")
        print("\033[1;35;40mRP - CARVALHOS\033[1;37;40m\t\t\t\t\033[1;35;40mRP - MATOSINHOS II\033[1;37;40m")
        print("Atlantic Retail Park Carvalhos\t\tCentro Comercial Mar Shopping")
        print("Rua da Presa Seca, nº36-38\t\tAvenida Óscar Lopes, Piso 0 - Loja 63")
        print("4415-307 Pedroso\t\t\tLeça da Palmeira 4450-337 Matosinhos")
        print("Ext: 4701-4708\t\t\t\tExt: 5101-5108")
        print("Código SA-135 | SAP - 1129\t\tCódigo SA-144 | SAP - 1130\n")
        print("\033[1;35;40mRP - ERMESINDE\033[1;37;40m\t\t\t\t\033[1;35;40mRP - PENAFIEL\033[1;37;40m")
        print("IN Ermesinde Retail Park\t\tCity Park Penafiel")
        print("Av. Eng.º Duarte Pacheco - Lojas 12/13\tLugar do Tapadinho - Loja C")
        print("4445-416 Ermesinde\t\t\t4560-162 Guilhufe")
        print("Ext: 5601-5608\t\t\t\tExt: 3101-3108")
        print("Código SA-234 | SAP - 1137\t\tCódigo SA-286 | SAP - 1149\n")
        print("\033[1;35;40mRP - GAIA\033[1;37;40m\t\t\t\t\033[1;35;40mRP - PORTO\033[1;37;40m")
        print("Rua Camilo Castelo Branco, 787\t\tLa Vie Baixa")
        print("Santa Marinha\t\t\t\tRua Fernandes Tomás, Piso 0 - Loja 005")
        print("4400-062 V.N.Gaia\t\t\t4000-211 Porto")
        print("Ext: 4001-4008\t\t\t\tExt: 1801-1808")
        print("Código SA-073 | SAP - 1114\t\tCódigo SA-278 | SAP - 1145\n")
        q = input("")
        os.system('clear')
        print("\033[1;37;45mRP - Grande Porto(Enter->Sair)\n")
        print("\033[1;35;40mRP - MAIA\033[1;37;40m")
        print("Estrada Nacional 14 (Km 7)")
        print("Lugar do Chiolo - Barca")
        print("Apartado 1264, 4475-045 Maia")
        print("Ext: 1201-1208")
        print("Código SA-007 | SAP - 1101\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        q = input("")
        os.system('clear')
        c = None
      elif q == 4:
        print("\033[1;37;45mRP - Zona Centro(Enter->Avançar)\n")
        print("\033[1;35;40mRP - ALMEIRIM\033[1;37;40m\t\t\t\t\033[1;35;40mRP - AVEIRO\033[1;37;40m")
        print("Edifício Pingo Doce\t\t\tAveiro Retail Park")
        print("EN.114 - Quinta da Alorna\t\tZona Industrial Taboeira")
        print("Zona Industrial de Almeirim, 61\t\tLote F")
        print("2080-221 Almeirim\t\t\t3800-055 Aveiro")
        print("Ext: 2301-2308\t\t\t\tExt: 1701-1708")
        print("Código SA-284 | SAP - 1148\t\tCódigo SA-129 | SAP - 1126\n")
        print("\033[1;35;40mRP - CALDAS DA RAINHA\033[1;37;40m\t\t\t\033[1;35;40mRP - COIMBRA\033[1;37;40m")
        print("Centro Comercial La Vie\t\t\tParque Mondego")
        print("R.Belchior de Matos,nº11,piso0-Loja015\tEN. 1-7 - Loja H-T")
        print("2500-324 Caldas da Rainha\t\tApartado 188 - 3001-903 Coimbra")
        print("Ext: 5401-5408\t\t\t\tExt: 3301-3308")
        print("Código SA-148 | SAP - 1132\t\tCódigo SA-030 | SAP - 1107\n")
        print("\033[1;35;40mRP - POMBAL\033[1;37;40m\t\t\t\t\033[1;35;40mRP - PORTO DE MÓS\033[1;37;40m")
        print("Edifício Intermaché Pombal\t\tAtlantic Retail Park")
        print("Rua Marechal António de Spínola-Loja 3\tE.N.1, KM 105, Pedreiras - Loja D")
        print("3100-389 Pombal\t\t\t\t2480-109 Porto de Mós")
        print("Ext: 6201-6208\t\t\t\tExt: 5501-5508")
        print("Código SA-272 | SAP - 1142\t\tCódigo SA-230 | SAP - 1135")
        q = input("")
        os.system('clear')
        print("\033[1;37;45mRP - Zona Centro(Enter->Avançar)\n")
        print("\033[1;35;40mRP - COVILHÃ\033[1;37;40m\t\t\t\t\033[1;35;40mRP - GUARDA\033[1;37;40m")
        print("Covilhã Shopping\t\t\tIN Guarda Retail Park")
        print("Alameda Pêro da Covilhã - Loja 17\tParque Industrial")
        print("Quinta do Alvito\t\t\tLoja 4")
        print("6200-251 Boidobra - Covilhã\t\t6300-625 Guarda")
        print("Ext: 6101-6108\t\t\t\tExt: 2201-2208")
        print("Código SA-270 | SAP - 1141\t\tCódigo SA-282 | SAP - 1147\n")
        print("\033[1;35;40mRP - LEIRIA\033[1;37;40m\t\t\t\t\033[1;35;40mRP - OVAR\033[1;37;40m")
        print("Edifício Intermraché de Leiria\t\tAtlantic Park Ovar")
        print("Rua das Olhavas - Loja 9\t\tEN 109 - Lugar da Pardala - Loja L")
        print("2410-197 Leiria\t\t\t\t3880-728 Ovar")
        print("Ext: 1901-1908\t\t\t\tExt: 2801-2808")
        print("Código SA-274 | SAP - 1143\t\tCódigo SA-124 | SAP - 1125\n")
        print("\033[1;35;40mRP - TORRES NOVAS\033[1;37;40m\t\t\t\033[1;35;40mRP - VISEU\033[1;37;40m")
        print("Torreshopping\t\t\t\tPalacio do Gelo Shopping")
        print("Ponte Nova-Nicho dos Riachos-Loja A02\tQuinta da Alagoa, Piso 0 - Loja 21")
        print("2350-600 Torres Novas\t\t\t3500-606 Viseu")
        print("Ext: 4401-4408\t\t\t\tExt: 3201-3208")
        print("Código SA-103 | SAP - 1118t\t\tCódigo SA-138 | SAP - 1127")
        q = input("")
        os.system('clear')
        print("\033[1;37;45mRP - Zona Centro(Enter->Sair)\n")
        print("\033[1;35;40mRP - SANTARÉM\033[1;37;40m")
        print("Santarém Retail Park")
        print("Quinta das Cegonhas, Estrada Nac.3 - Lote 28 - Unidade C")
        print("2000-471 Santarém")
        print("Ext: 3401-3408")
        print("Código SA-141 | SAP - 1128\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        q = input("")
        os.system('clear')
        c = None
      elif q == 5:
        print("\033[1;37;45mRP - Grande Lisboa(Enter->Avançar)\n")
        print("\033[1;35;40mRP - ALFRAGIDE\033[1;37;40m\t\t\t\t\033[1;35;40mRP - ALVERCA\033[1;37;40m")
        print("Av. dos Cavaleiros, 67 e 67-A\t\tAlfandega Park Alverca")
        print("2790-460 Carnanxide\t\t\tE.N.10, Km 127,2-Loja 3\nOeiras\t\t\t\t\tAlverca do Ribatejo")
        print("Ext: 5701-5708\t\t\t\t2615-351 Vila Franca de Xira")
        print("Código SA-132 | SAP - 1133\t\tExt: 5901-5908")
        print("\t\t\t\t\tCódigo SA-236 | SAP - 1139\n")
        print("\033[1;35;40mRP - BARREIRO\033[1;37;40m\t\t\t\t\033[1;35;40mRP - LISBOA\033[1;37;40m")
        print("Barreiro Retail Planet\t\t\tCentro Comercial Campo Pequeno")
        print("E.N.10,Km 18,5-Zona Ind. Coina-Loja-D\tPraça Touros, Piso 1 - Loja 101")
        print("2830-411 Coina - Barreiro\t\t1000-082 Lisboa")
        print("Ext: 5801-5808\t\t\t\tExt: 2101-2108")
        print("Código SA-232 | SAP - 1136\t\tCódigo SA-280 | SAP - 1146\n")
        print("\033[1;35;40mRP - LOURES\033[1;37;40m\t\t\t\t\033[1;35;40mRP - OLIVAIS\033[1;37;40m")
        print("Centro Comercial Continente de Loures\tSpacio Shopping,Piso 1-Loja 1.39/2.27")
        print("E.N.250,Quinta Casal da Pipa-Loja 72\tRua Cidade de Bolama,n.º4")
        print("2670-600 Loures\t\t\t\t1800-079 Lisboa")
        print("Ext: 1001-1008\t\t\t\tExt: 5301-5308")
        print("Código SA-026 | SAP - 1106\t\tCódigo SA-146 | SAP - 1131")
        q = input("")
        os.system('clear')
        print("\033[1;37;45mRP - Grande Lisboa(Enter->Sair)\n")
        print("\033[1;35;40mRP - MAFRA\033[1;37;40m\t\t\t\t\033[1;35;40mRP - MONTIJO\033[1;37;40m")
        print("Mafra Retail Park\t\t\tForum Montijo")
        print("R.Comendador José Noronha Gorjão\tZona Industrial do Pau Queimado")
        print("Quinta das Pevides - Loja B\t\tArmazém D - Rua da Azinheira")
        print("2640-408 Mafra\t\t\t\t2870-100 Montijo")
        print("Ext: 6001-6008\t\t\t\tExt: 3501-3508")
        print("Código SA-238 | SAP - 1140\t\tCódigo SA-035 | SAP - 1108\n")
        print("\033[1;35;40mRP - SETÚBAL\033[1;37;40m\t\t\t\t\033[1;35;40mRP - SINTRA\033[1;37;40m")
        print("Atlantic Park\t\t\t\tSintra Retail Park")
        print("Av.Mestre Lima Freitas\t\t\tApartado 9 E.N. 249/I.C.19 - Loja 10/11\nEstrada de Algeruz - Armazém D\t\tAlto do Forte")
        print("2910-279 Setúbal\t\t\t2636-901 Rio de Mouro")
        print("Ext: 3601-3608\t\t\t\tExt: 1401-1408")
        print("Código SA-045 | SAP - 1109\t\tCódigo SA-011 | SAP - 1103")
        print("\n\n\n\n\n")
        q = input("")
        os.system('clear')
        c = None
      elif q == 6:
        print("\033[1;37;45mRP - Zona Sul(Enter->Sair)\n")
        print("\033[1;35;40mRP - ALBUFEIRA\033[1;37;40m\t\t\t\t\033[1;35;40mRP - FARO\033[1;37;40m")
        print("Retail Park Albufeira\t\t\tFaro Shopping")
        print("Lugar da Tavagueira-Guia-Armazém E\tEstrada Nacional 125 - Km 103")
        print("8200-425 Albufeira\t\t\t8005-145 Faro")
        print("Ext: 3701-3708\t\t\t\tExt: 3001-3008")
        print("Código SA-055 | SAP - 1110\t\tCódigo SA-053 | SAP - 1134\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        q = input("")
        os.system('clear')
        c = None
      elif q == 7:
        print("\033[1;37;45mRP - Ilhas(Enter->Sair)\n")
        print("\033[1;35;40mRP - AÇORES I\033[1;37;40m\t\t\t\t\033[1;35;40mRP - AÇORES II\033[1;37;40m")
        print("Estrada S. Gonçalo - Fajã de Baixo\tParque Industrial da Achada")
        print("9500-435 Ponta Delgada\t\t\tAvenida Visconde Bruges-Lote 17")
        print("Ext: 2601-2608\t\t\t\t9700-135 Angra do Heroísmo")
        print("Código SA-240 | SAP - 1138\t\tExt: 2001-2008")
        print("\t\t\t\t\tCódigo SA-111 | SAP - 3101\n")
        print("\033[1;35;40mRP - MADEIRA\033[1;37;40m\t\t\t\t\033[1;35;40mRP - MADEIRA II\033[1;37;40m")
        print("C.Comercial Cancela Park\t\tRua 5 de Outubro nº 92\nPiso 0, Loja 27,28 e 29\t\t\t9000-216 Funchal")
        print("Estrada do Garajau - Cancela\t\tExt: 4801-4808")
        print("9125-067 Caniço - Funchal\t\tCódigo SA-060 | SAP - 1111")
        print("Ext: 3801-3808\nCódigo SA-294 | SAP - 1153\n")
        print("\033[1;35;40mRP - ARMAZÉM AÇORES\033[1;37;40m\t\t\t\033[1;35;40mRP - ARMAZÉM MADEIRA\033[1;37;40m")
        print("Estrada Regional, nº3, Ribeira Seca\tSitio da Ribeira dos Pretetes")
        print("9600-213 Ribeira Grande\t\t\t1ª Impasse do Pinheiro")
        print("Ponta Delgada\t\t\t\t9125-155 Caniço - Madeira")
        print("Ext: 2701\t\t\t\tExt: 3850-3855")
        print("Código SA-042 | SAP - 1004\t\tCódigo SA-062 | SAP - 1002")
        q = input("")
        os.system('clear')
        c = None
      else:
        c = None
    elif c == 5:
      print("\033[1;35;40mRP - TOOLKIT\nVersion 1.4.01 Beta\nBuild by Dk0der(Diogo Vilaça - PTJ) 2017\nemail: realplayerzero@gmail.com")
      print("\033[1;36;40mPrima enter para sair...\033[1;37;40m")
      q = input("")
      os.system('clear')
      c = None
    elif c == 6:
      exit_program()
    else:
      os.system('clear')
      c = None
	
         
  except ValueError:
    print("")
    os.system('clear')
    c = None