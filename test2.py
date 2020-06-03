def get_vat(payment):
	try:
		payment = float(payment)
		vat = payment / 100 * 13
		vat =  round(vat, 2)
		return "Вот это у тебя нагло спиздит государство на кокс: {}".format(vat)
	except (TypeError, ValueError):
		return "Таких зарплат не бывает долбаеб!"

def get_vat2(payment):
	try:
		payment = float(payment)
		vat = payment / 100 * 13
		vat =  round(vat, 2)
		return vat
	except (TypeError, ValueError):
		return "Таких зарплат не бывает долбаеб!"

cash = input('какие цыфры в твоей жалкой зп? (без вычета налога) ')
result = get_vat(cash)
result2 = get_vat2(cash)
print(result)
clock = input('а сколько часов ты ишачил на этих убблюдков сверхурочно? ')
day = input('сколько дней тебя эксплуатировали как вещь? (без переработок) ')
summa_vuchet = int(cash) - result2
print('тебе капнет значит: ', summa_vuchet)
summa_den = summa_vuchet / int(day)
summa_den = round(summa_den, 2)
summa_chas = (summa_den / 8) * 2
print('твой час свыше нормы стоил: ', summa_chas)
summa_per = summa_chas * int(clock)
print('выходит ты нещадил себя за какие то: ', summa_per)
summa_all = summa_vuchet + summa_per

print('Вот что по праву твое:', summa_all )
print('Ну не все так плохо да?')
avans = input ('Сколько ты из этого всадил с аванса? ')
itog = summa_all - int(avans)
print('Получишь значит ', itog ,'капейки, на большее ты не спасобен...')