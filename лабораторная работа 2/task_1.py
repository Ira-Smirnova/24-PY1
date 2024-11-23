money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count_month = 0 # Счётчик месяцев

while money_capital > 0:
    excess = spend - salary # Превышение покрытия расходов
    money_capital -= excess
    if money_capital > 0:
        count_month += 1
    spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", count_month)
