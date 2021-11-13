from time import sleep
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos quer financiar? '))
print('PROCESSANDO...')
sleep(2)
prestacao = casa / (anos * 12)
if prestacao < (30 * salario / 100):
    print('Empréstimo \033[32mCONCEDIDO\033[m!')
else:
    print('Empréstimo \033[31mNEGADO\033[m!')
print('Para pagar uma casa de \033[32mR${:.2f}\033[m em \033[31m{}\033[m anos'.format(casa, anos), end='')
print(' a prestação será de \033[32mR${:.2f}\033[m!'.format(prestacao))