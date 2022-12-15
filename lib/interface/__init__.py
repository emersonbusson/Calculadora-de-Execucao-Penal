def Leia_Int(mensagem):
    while True:
        try:
            numero = int(input(mensagem))

        except (ValueError, TypeError):
            print(f'\33[31mPor favor, digite um número inteiro válido!\33[m')
            continue
        except KeyboardInterrupt:
            print('\33[35mO úsuario preferiu não digitar esse número.\33[m')
            print()
            return 0
        else:
            return numero



def Linha(tamanho = 42):
    linha_caractere = '-' * tamanho
    return linha_caractere


def Cabecalho(texto, tam=0):
    print(Linha(tamanho=len(texto)))
    print(f'\33[7m{str(texto).center(len(texto))}\33[m')
    print(Linha(tamanho=len(texto)))

def Menu(lista):
    Cabecalho('MENU PRINCIPAL',tam=65)
    cont = 1
    for item in lista:
        print(f'\33[33m{cont}\33[m - \33[34m{item}\33[m')
        cont += 1
    print(Linha(tamanho=65))
    opção = Leia_Int('\33[32mSua opção: \33[m')
    return opção

###
def Fracao_1(dias):               #oque é uma fração? é uma representação da divisão entre dois números.
    # dias é o numerador
    # definição de "denominador":  é por quanto o numerador vai ser dividido

    denominador = [2, 3, 4, 5, 6]
    for divisor in denominador:
        print(f'\33[31m1/{divisor} tem um total de: {dias / divisor:1.1f} dias.\33[m')


def Fracao_2_3_5_11(dias):
    numerador = [2,2,3,3,5,11]
    demominador = [3,5,5,8,12,24]
    x = 0
    for divisor in demominador:
        print(f'\33[32m{numerador[x]}/{demominador[x]} tem o total de: {numerador[x] * (dias / divisor):1.1f} dias.\33[m')
        x += 1


def Porcentagem(dias):
    porcento = [16,20,25,30,40,50,60,70]
    x = 0
    for elemento in porcento:
        print(f'PORCENTAGEM em \33[35m{elemento}%\33[m: \33[31m{dias * elemento / 100}\33[m')
        x += 1


def Anos_para_dias(anos=0, meses=0,dias=0):
    quantidade_dias_ano = anos * 365
    quantidade_dias_mes = meses * 30
    quantidade_dias_dias = dias
    total = (quantidade_dias_ano + quantidade_dias_mes + quantidade_dias_dias)
    return total


def Dias_para_anos(dias=0):
    anos, dias = dias // 365, dias % 365
    meses, dias = dias // 30, dias % 30
    print(f'{anos} anos, {meses} meses, {dias} dias')
###