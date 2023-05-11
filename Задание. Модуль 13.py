ticket = int(input("Введите кол0во билетов:"))
price = 0

for i in range(ticket):
    i += 1
    while True:
            ticket_age = int(input(f'Для какого возраста билет №{i}? '))
            if ticket_age < 18:
                price +=0
            elif 18 <= ticket_age < 25:
                price += 990
            else:
                ticket_age >= 25
                price += 1390
            if type(ticket_age) == int:
                break
if ticket_age > 3:
    price = (price * 0.90)
    print("Ваша цена с учетом скидки", price, "Руб.")
else:
    print("Стоимость билетов", price, "Руб.")