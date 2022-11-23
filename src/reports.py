import random as rnd
import data as dt


def salary_report(timestamp, data):
    worker = rnd.choice(data.workers)

    return f'''\
    {timestamp}: Отчёт о выданной заработной плате
    Получатель: {worker.name}, {worker.position} отдела {worker.department}
    Сумма: {worker.salary} руб. 00 коп.
    Уплаченный налог: {round(worker.salary * 0.13)} руб. 00 коп.'''


def bonus_report(timestamp, data):
    worker = rnd.choice(data.workers)
    reason = rnd.choice(data.bonus_reasons)
    bonus = rnd.randint(10000, 150000)

    return f'''\
    {timestamp}: Отчёт о выданной премии
    Получатель: {worker.name}, {worker.position} отдела {worker.department}
    Сумма: {bonus} руб. 00 коп.
    Основание выдачи премии: {reason}'''


def fine_report(timestamp, data):
    worker = rnd.choice(data.workers)
    reason = rnd.choice(data.fine_reasons)
    fine = rnd.randint(500, 50000)

    return f'''\
    {timestamp}: Отчёт о взысканном штрафе
    Ответчик: {worker.name}, {worker.position} отдела {worker.department}
    Сумма: {fine} руб. 00 коп.
    Основание взыскания штрафа: {reason}'''


def complaint_report(timestamp, data):
    worker1 = rnd.choice(data.workers)
    worker2 = rnd.choice(data.workers)
    reason = rnd.choice(data.complaint_reasons)

    return f'''\
    {timestamp}: Отчёт о внутренней жалобе
    Истец: {worker1.name}, {worker1.position} отдела {worker1.department}
    Ответчик: {worker2.name}, {worker2.position} отдела {worker2.department}
    Причина жалобы: {reason}'''


def oil_sale_report(timestamp, data):
    country = rnd.choice(data.countries)
    volume = rnd.randint(10000, 50000)
    discount = round(rnd.uniform(0.01, 0.05), 4)
    price = round(volume * data.oil_prices[country] * (1 - discount))
    tax = 0.26

    return f'''\
    {timestamp}: Отчёт о продаже сырья
    Покупатель: {data.companies[country]}, {country}
    Объём сделки: {volume} барр.
    Скидка: {round(discount*100, 2)}%
    Сумма сделки: {price} руб. 00 коп.
    Уплаченный налог: {round(price * tax)} руб. 00 коп.'''


def equipment_buy_report(timestamp, data):
    country, company = rnd.choice(list(data.companies.items()))
    equipment = rnd.choice(data.equipments)
    amount = rnd.randint(1, 5)
    price = round(data.eq_prices[(company, equipment)] * amount)
    tax = 0.37

    return f'''\
    {timestamp}: Отчёт о покупке оборудования
    Продавец: {company}, {country}
    Оборудование: {equipment}, {amount} шт.
    Сумма сделки: {price} руб. 00 коп.
    Уплаченная таможенная пошлина: {round(price * tax)} руб. 00 коп.'''

def equipment_transfer_report(timestamp, data):
    rig = rnd.choice(data.rigs)
    equipment = rnd.choice(data.equipments);
    amount = rnd.randint(1, 5);
    transfer_way = rnd.choice(data.transfer_ways)
    price = round(data.eq_transfer_prices[(rig, equipment, transfer_way)] * amount)

    return f'''\
    {timestamp}: Отчёт о трансфере оборудования
    Пункт назначения: {rig} нефтяная вышка
    Оборудование: {equipment}, {amount} шт.
    Способ трансфера: {transfer_way}
    Затраты: {price} руб. 00 коп.'''

def oil_transfer_report(timestamp, data):
    rig = rnd.choice(data.rigs)
    storage = rnd.choice(data.storages)
    volume = rnd.randint(10000, 50000)
    price = round(data.oil_transfer_prices[(rig, storage)] * volume)

    return f'''\
    {timestamp}: Отчёт о трансфере сырья
    Пункт отправления: {rig} нефтяная вышка
    Пункт назначания: {storage} нефтехранилище
    Объём трансфера: {volume} барр.
    Затраты: {price} руб. 00 коп.'''


def rig_lawsuit_report(timestamp, data):
    rig = rnd.choice(data.rigs)
    plaintiff = rnd.choice(data.plaintiffs)
    claim = rnd.choice(data.rig_claims)
    flag, result = rnd.choice(list(data.lawsuit_results.items()))
    price = rnd.randint(10000, 100000) * (100 if flag else 1)

    return f'''\
    {timestamp}: Отчёт о судебном иске к деятельности вышки
    Истец: {plaintiff}
    Ответчик: {rig} нефтяная вышка
    Суть иска: {claim}
    Вердикт: {result}
    Затраты: {price} руб. 00 коп.'''


def company_lawsuit_report(timestamp, data):
    plaintiff = rnd.choice(data.plaintiffs)
    claim = rnd.choice(data.company_claims)
    flag, result = rnd.choice(list(data.lawsuit_results.items()))
    price = rnd.randint(10000, 100000) * (10000 if flag else 10)

    return f'''\
    {timestamp}: Отчёт о судебном иске к деятельности компании
    Истец: {plaintiff}
    Суть иска: {claim}
    Вердикт: {result}
    Затраты: {price} руб. 00 коп.'''


def ad_report(timestamp, data):
    country = rnd.choice(data.countries)
    ad_type = rnd.choice(data.ad_types)
    price = round(data.ad_prices[(country, ad_type)])
    gain = round(price * (2 ** rnd.uniform(-1.00, 5.00)))

    return f'''\
    {timestamp}: Отчёт о проведенной рекламной компании
    Страна проведения: {country}
    Способ рекламы: {ad_type}
    Затраты: {price} руб. 00 коп.
    Доход: {gain} руб. 00 коп.'''


reports = [
    salary_report,
    bonus_report,
    fine_report,
    complaint_report,
    oil_sale_report,
    equipment_buy_report,
    equipment_transfer_report,
    oil_transfer_report,
    rig_lawsuit_report,
    company_lawsuit_report,
    ad_report]
