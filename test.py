

slovar = dict()

slovar['Дмитрий'] = 'в Пушкино'
slovar['Ренат'] = 'сдох к хуям'
slovar['Студент'] = 'в Ивантеевке'
slovar['Юрец'] = 'скоро откинется'

namewrite = input('Введите имя кого ищите: ')

if namewrite in slovar:
	print ('Этот хуй ' + slovar.get(namewrite))
else:
	print ('Человека каторого вы ищите не найти' + ', ' + namewrite + ' несуществовал')