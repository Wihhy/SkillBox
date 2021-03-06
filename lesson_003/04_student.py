# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

needed_money_for_year = 0
educational_grant_for_year = educational_grant * 10
i = 2
while i < 10:
    inflation = (expenses / 100) * 3
    expenses = expenses + inflation
    needed_money_for_year += expenses
    i += 1
credit = needed_money_for_year - educational_grant_for_year
print('Студенту нужно попросить', round(credit, 2), 'грн')
