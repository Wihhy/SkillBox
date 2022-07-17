
def profit_counter():
    sold_sum = 0
    bought_sum = 0
    while True:
        deal = input('Введи сделки по одному, а когда закончишь напиши "y":\n')
        if '+' in deal:
            bought_sum += float(deal[:-1])
            continue
        elif '-' in deal:
            sold_sum += float(deal[:-1])
            continue
        elif deal == 'y':
            break
        return sold_sum, bought_sum
    if sold_sum > bought_sum:
        profit = bought_sum / 100 * 2
    elif sold_sum < bought_sum:
        profit = sold_sum / 100 * 2
    print(f'За день было продано на {sold_sum} евро;\n'
          f'За день было куплено на {bought_sum} евро;\n'
          f'Суммарный оборот {sold_sum + bought_sum} евро;\n'
          f'Профит составляет: {profit} евро.\n')


profit_counter()
