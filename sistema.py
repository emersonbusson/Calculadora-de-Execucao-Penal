from lib.interface import *
from time import sleep
from datetime import  datetime, timedelta


# Cabecalho('''Dr Agenor Loiola - Advocacia Especializada e Consultoria Jurídica''')
while True:
      resposta = Menu(['Converta anos e meses para dias',
      'Converta de dias para anos e meses',
      'Converta os dias em frações e porcentagens',
      'Some ou subtraía dias de uma Data',
      'Calcule a diferença entre duas datas',
      'PARA SAIR'])
      if resposta == 1:
            Cabecalho('Converta anos e meses para dias')
            anos = Leia_Int('Digite a quantidade de anos: ')
            meses = Leia_Int('Digite a quantidade de meses: ')
            dias = Leia_Int('Digite a quantidade de dias: ')
            print(f'Total convertido em dias: \33[34m{Anos_para_dias(anos=anos, meses=meses,dias=dias)}\33[m')
      elif resposta == 2:
            Cabecalho('Converta de dias para anos e meses')
            dias = Leia_Int("Digite a quantidade de dias: ")
            Dias_para_anos(dias)
      elif resposta == 3:
            Cabecalho('Converta os dias em frações e porcentagens')
            dias = Leia_Int('Digite a quantidade de dias: ')
            Fracao_1(dias)
            Fracao_2_3_5_11(dias)
            Porcentagem(dias)
      elif resposta == 4:
            Cabecalho('Some ou subtraía dias de uma Data')
            print('\33[7mDigite a data neste formato: 00/00/0000\33[m')
            while True:
                  try:
                        data_1 = str(input('\33[32mData do Calculo: \33[m'))[:10].strip().lower()
                        dias = Leia_Int('digite a quantidade de dias a somar e subtrair: ')
                        data_1 = datetime.strptime(data_1, "%d/%m/%Y")
                        soma = data_1 + timedelta(days=dias)
                        print(f'\33[31mSomando:\33[m \33[34m{dias}\33[m dias na data: \33[34m{data_1.strftime("%d/%m/%Y")}\33[m\n\33[33mNova data: {soma.strftime("%d/%m/%Y")}\33[m')
                        sub = data_1 - timedelta(days=dias)
                        print(f'\33[31mSubtraindo:\33[m \33[34m{dias}\33[m dias na data: \33[34m{data_1.strftime("%d/%m/%Y")}\33[m\n\33[33mNova data: {sub.strftime("%d/%m/%Y")}\33[m')
                        break
                  except (ValueError, TypeError):
                        print('\33[7mDigite a data neste formato: 00/00/0000\33[m')
                  except (KeyboardInterrupt):
                        print('\33[35mO úsuario preferiu não digitar esse número.\33[m')
                        break
      elif resposta == 5:
            Cabecalho('Calcule a diferença entre duas datas')
            print('\33[7mDigite a data neste formato: 00/00/0000\33[m')
            print()
            while True:
                  try:
                        data_1 = str(input('\33[32mData 1: \33[m'))[:10].strip().lower()
                        data_1 = datetime.strptime(data_1, "%d/%m/%Y")
                        data_2 = str(input('\33[33mData 2: \33[m'))[:10].strip().lower()
                        data_2 = datetime.strptime(data_2, "%d/%m/%Y")
                        if data_1 <= data_2:
                              print(f'\33[7mA data 1 não pode ser menor ou igual a data 2.\33[m')
                        else:
                              difereca_dias = data_1 - data_2
                              print(f'A diferença de entre as duas datas em dias é: \33[34m{difereca_dias.days}\33[m dias.')
                              break
                  except (ValueError, TypeError):
                        print('\33[7mDigite a data neste formato: 00/00/0000\33[m')
                  except (KeyboardInterrupt):
                        print('\33[35mO úsuario preferiu não digitar esse número.\33[m')
                        break
      elif resposta == 6:
            print('\33[7m\nSaindo do sistema... Até logo!\33[7m\n')
            break
      else:
            print('\33[31mErro! Digite um opção válida.\33[m')
      sleep(0.7)
