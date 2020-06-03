

slovar = dict()

slovar['Дмитрий'] = 
slovar['Ренат'] = 
slovar['Студент'] = 
slovar['Юрец'] = 

namewrite = input('Введите имя кого ищите: ')

if namewrite in slovar:
	print ('Этот ' + slovar.get(namewrite))
else:
	print ('Человека каторого вы ищите не найти' + ', ' + namewrite + ' несуществовал')