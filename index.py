import datetime
nasc =int(input('Digite o ano do seu nascimento:'))
datetime =datetime.datetime.now()
date = datetime.date()
ano =int(date.strftime("%Y"))
idade = ano - nasc
if idade < 18:
    print('Faltam {} anos para o seu alistamento'.format(18 - idade))
elif idade == 18:
    print('Você precisa se alistar esse ano')
else:
    print('Você deveria ter se alistado a {} anos' .format(idade - 18))