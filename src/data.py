import random as rnd
import itertools as it

def combine2(A, B):
    for a in A:
        for b in B:
            yield (a, b)


def combine3(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                yield(a, b, c)
    

class Worker:

    def __init__(self, name, department, position, salary):
        self.name = name
        self.department = department
        self.position = position
        self.salary = salary


class Data:
        
    def __init__(self):
        self.first_names_m = ['Григорий', 'Лев', 'Андрей', 'Роман', 'Арсений', 'Степан', 'Владислав', 'Никита', 'Глеб', 'Марк']
        self.first_names_f = ['Анастасия', 'Анна', 'Мария', 'Елена', 'Дарья', 'Алина', 'Ирина', 'Екатерина', 'Арина', 'Полина']
        self.last_names = ['Смирнов', 'Иванов', 'Кузнецов', 'Соколов', 'Попов', 'Лебедев', 'Козлов', 'Новиков', 'Морозов', 'Петров']

        self.departments = ['маркетинга', 'стратегии', 'кадров', 'финансов', 'логистики', 'юриспруденции', 'производства']
        self.positions = ['стажёр', 'сотрудник', 'старший сотрудник', 'менеджер', 'заместитель начальника']
        
        self.generate_salaries()
        self.generate_workers()

        self.countries = ['Беларусь', 'Казахстан', 'Грузия', 'Китай']
        self.oil_prices = dict(zip(self.countries, [rnd.uniform(5000.00, 8000.00) for _ in range(len(self.countries))]))

        self.bonus_reasons = ['выдающиеся результаты труда', 'значительное перевыполнение рабочего плана', 'отличное качество работы']
        self.fine_reasons = ['неудовлетворительные результаты труда', 'невыполнение плана работы', 'порча имущества']
        self.complaint_reasons = ['неисполнение обязанностей', 'пренебрежение техникой безопасности на рабочем месте', 'некорпоративное поведение', 'нарушение должностных полномочий']
        
        self.companies = dict(zip(self.countries, ['ООО "Картофель-Ойл"', 'ПАО "Кумыснефтьгаз"', 'ООО "Аджиканефть"', 'ПАО "Пекин Ойл Холдинг"']))
        self.equipments = ['генератор', 'насос', 'ротор', 'двигатель']
        self.generate_eq_prices()
        
        self.rigs = ['Приобская', 'Урьевская', 'Имилорская', 'Арланская']
        self.transfer_ways = ['поезд', 'автомобиль', 'самолёт']
        self.generate_eq_transfer_prices()

        self.storages = ['Смоленское', 'Иркутское', 'Архангельское']
        self.generate_oil_transfer_prices()

        self.plaintiffs = ['ПАО "Нефтегаз"', 'ООО "Газонефть"', 'ОАО "Росметан"', 'ПАО "Губкин"']
        self.rig_claims = ['Нарушение экологических норм', 'Нарушение правил техники безопасности']
        self.company_claims = ['Невыполнение обязательств', 'Уклонение от уплаты налогов', 'Нарушение антмонопольного законодательства']
        self.lawsuit_results = {True: 'удовлетворить требования истца', False: 'отклонить требования истца'}

        self.ad_types = ['реклама на радио и телевидении', 'реклама в социальных сетях', 'таргетированная реклама', 'печатная реклама', 'сувенирная реклама']
        self.generate_ad_prices()
        
    
    def generate_salaries(self):
        self.salaries = dict()
        for department in self.departments:
            self.salaries[department] = dict()

            for i, position in enumerate(self.positions):
                self.salaries[department][position] = (i+1) * 30000 + rnd.randint(-10000, 10000)


    def generate_workers(self):
        self.workers = [];
        for last_name in self.last_names:
            for first_name in self.first_names_m:
                name = f'{last_name} {first_name}'
                department = rnd.choice(self.departments)
                position = rnd.choice(self.positions)
                salary = self.salaries[department][position]

                self.workers.append(Worker(name, department, position, salary))

            for first_name in self.first_names_f:
                name = f'{last_name}а {first_name}'
                department = rnd.choice(self.departments)
                position = rnd.choice(self.positions)
                salary = self.salaries[department][position]

                self.workers.append(Worker(name, department, position, salary))

    
    def generate_eq_prices(self):
        keys = list(combine2(self.companies.values(), self.equipments))
        self.eq_prices = dict(zip(keys, 
                                  map(lambda x: rnd.uniform(50000.00, 1000000.00), keys)))


    def generate_eq_transfer_prices(self):
        keys = list(combine3(self.rigs, self.equipments, self.transfer_ways))
        self.eq_transfer_prices = dict(zip(keys, 
                                  map(lambda x: rnd.uniform(20000.00, 100000.00), keys)))
        
    
    def generate_oil_transfer_prices(self):
        keys = list(combine2(self.rigs, self.storages))
        self.oil_transfer_prices = dict(zip(keys, 
                                  map(lambda x: rnd.uniform(5.00, 50.00), keys)))
        
    
    def generate_ad_prices(self):
        keys = list(combine2(self.countries, self.ad_types))
        self.ad_prices = dict(zip(keys, 
                                  map(lambda x: rnd.uniform(1000000.00, 10000000.00), keys)))
