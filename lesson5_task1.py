# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import namedtuple, Counter

CompanyNew = namedtuple('CompanyNew', 'name, first_quarter, second_quarter, third_quarter, fourth_quarter')
companies = Counter()
all_quarters = 0

number_of_companies = int(input('Сколько всего будет компаний? '))

for i in range(number_of_companies):
    name = input('Как называется компания? ')
    first_quarter = int(input('Сколько она заработала в первом квартале? '))
    second_quarter = int(input('Сколько во втором? '))
    third_quarter = int(input('Сколько в третьем? '))
    fourth_quarter = int(input('А в четвертом? '))
    all_quarters += first_quarter + second_quarter + third_quarter + fourth_quarter
    company = CompanyNew(name, first_quarter, second_quarter, third_quarter, fourth_quarter)
    companies[company.name] = company.first_quarter, company.second_quarter, company.third_quarter, company.fourth_quarter

average_profit = all_quarters / number_of_companies

list_of_profit = list(companies.values())
list_of_profit_names = list(companies.keys())
list_of_profitable = []
list_of_unprofitable = []

for i in range(number_of_companies):
    if (list_of_profit[i][0] + list_of_profit[i][1] + list_of_profit[i][2] + list_of_profit[i][3]) > average_profit:
        list_of_profitable.append(list_of_profit_names[i])
    elif (list_of_profit[i][0] + list_of_profit[i][1] + list_of_profit[i][2] + list_of_profit[i][3]) < average_profit:
        list_of_unprofitable.append(list_of_profit_names[i])

print('Вот список компаний с доходом выше среднего:')
print(*list_of_profitable, sep=', ')
print('А вот с доходом ниже среднего:')
print(*list_of_unprofitable, sep=', ')
