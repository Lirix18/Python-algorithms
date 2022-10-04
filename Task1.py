from collections import defaultdict


def profit_calculation(profit, num):
    profit_company = defaultdict(int)
    total_profit = 0
    above_average = ''
    below_average = ''
    for k, v in profit.items():
        for i in v:
            total_profit += float(i)
            profit_company[k] += float(i)
    total_profit = total_profit / num
    max_profit = max(profit_company.values())
    min_profit = min(profit_company.values())
    for k, v in profit_company.items():
        if v == max_profit:
            above_average = k
        elif v == min_profit:
            below_average = k

    return f'Средняя годовая прибыль всех предприятий: {total_profit}\n' \
           f'Предприятия, с прибылью выше среднего значения: {above_average}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {below_average}'


if __name__ == '__main__':
    number_enterprises = int(input('Введите количество предприятий: '))
    data_company = defaultdict(list)
    for _ in range(number_enterprises):
        name_company = input('Введите название компании: ')
        profit_quarter = input('через пробел введите прибыль данного предприятия'
                               'за каждый квартал(Всего 4 квартала): ').split()
        data_company[name_company] = profit_quarter

    print(profit_calculation(data_company, number_enterprises))
