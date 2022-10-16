salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

def needcapital(salary, spend, months, increase):
    money = 0
    for i in range(1, 11):
        money -= spend
        money += salary
        spend *= (1 + increase)
    return (round(-money))
print(needcapital(salary, spend, months, increase))
# TODO Оформить решение
