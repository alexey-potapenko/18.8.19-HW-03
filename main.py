inp_error = True
total_price = 0

while inp_error == True:
    #Ловим ошибки ввода
    try:
        no_tikets_req = int(input('Сколько билетов хотите приобрести: '))
    except ValueError as e:
        print('Введите количество билетов цифрами') #Быквы вместо цифр
    else:
        if no_tikets_req <= 0: #количество меньше 1
            print('Количество билетов не может быть меньше 1')
        else:
            inp_error = False
for tiket_no in range(1, no_tikets_req + 1):
    inp_error = True
    while inp_error == True:
        # Ловим ошибки ввода
        try:
            print('Введите возраст посетителя ', tiket_no, ': ', end="")
            tiket_age = float(input())
        except ValueError as e:
            print('Введите возраст цифрами') #Быквы вместо цифр
        else:
            if tiket_age < 0:   #возраст  меньше 0
                print('Возраст не может быть меньше 0')
            else:
                inp_error = False
    if tiket_age < 18:
        total_price += 0
    elif 18 <= tiket_age <= 25:
        total_price += 990
    else:
        total_price += 1390
#Применяем скидку на колличество человек
if no_tikets_req > 3:
    total_price *= 0.9

print('Сумма к оплате %i руб., %02d коп.' % (int(total_price), total_price - int(total_price)) )
