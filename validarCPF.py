# input que sera mostrado ao usuario
print('Validador de CPF, digite um CPF, ou digite \'sair\' para encerrar o programa\n')

while True:
    cpf = input("Informe o CPF:\n")  # cpf a ser validado

    if len(cpf) == 11:
        soma = 0

        # verificação do primeiro digito
        for i, valor in enumerate(range(10, 1, -1)):
            multiplicacao = int(cpf[i]) * int(valor)
            soma += multiplicacao

        digito1 = 11 - (soma % 11) if (11 - (soma % 11)) <= 9 else 0

        # verificação do segundo digito
        soma = 0
        for i, valor in enumerate(range(11, 1, -1)):
            multiplicacao = int(cpf[i]) * int(valor)
            soma += multiplicacao

        digito2 = 11 - (soma % 11) if (11 - (soma % 11)) <= 9 else 0

        cpf_temp = cpf[:-2] + str(digito1) + str(digito2)

        # validação do cpf completo
        if cpf_temp == cpf and cpf != (cpf[0] * 11):
            print(f'O CPF: {cpf} é um CPF válido.')
        else:
            print(f'O CPF: {cpf} não é um CPF válido.')
    elif cpf == 'sair':
        print('Programa Finalizado')
        break
    else:
        print(f'O valor informado possui {len(cpf)} digitos, o CPF requer 11 digitos\n')
