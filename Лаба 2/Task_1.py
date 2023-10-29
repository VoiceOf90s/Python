money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
money = money_capital

while money > 0:
    if months != 0:
        spend *= 1+increase
    money -= (spend - salary)
    if money > 0:
        months += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", months)
