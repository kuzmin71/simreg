#Эта программа симулирует регистрацию на современном сайте
print('Registration')
Log = str.lower(input('Логин: ')).replace(' ', '')
Email = str(input('E-mail: '))
Pass = str(input("Пароль: ")).replace(' ', '')
Pass1 = str(input("Пароль снова: ")).replace(' ', '')
if Pass != Pass1:
    print('Пароли не совпадают')
    print('Введите пароли еще раз:')
    while True:
        Pass = str(input("Пароль: ")).replace(' ', '')
        Pass1 = str(input("Пароль снова: ")).replace(' ', '')
        if Pass == Pass1:
            break
print('Ваш Логин:', Log,',', 'Ваш пароль:', Pass,',', 'Были отправлены на ваш E-mail.')