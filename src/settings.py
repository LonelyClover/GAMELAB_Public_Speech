import datetime as dtime


class Settings:

    output_file = 'doc.txt'
    n_reports = 1000
    start_time = dtime.datetime.fromisoformat('2022-12-01 12:00:00')


    def set_setting(self, name, value=None):
        match name:
            case 'Выходной файл':
                self.output_file = value
                print(f'    Выходной файл установлен: "{self.output_file}"')

            case 'Число отчётов':
                try:
                    self.n_reports = int(value)
                    print(f'    Число отчётов установлено: {self.n_reports}')
                except:
                    print(f'    Неверный формат. Настройка "{name}" установлена по умолчанию')

            case 'Начальное время':
                try:
                    self.start_time = dtime.datetime.fromisoformat(value)
                    print(f'    Начальное время установлено: {self.start_time}')
                except:
                    print(f'    Неверный формат. Настройка "{name}" установлена по умолчанию')

            case _:
                print(f'    Незвестная настройка "{name}"')
    

    def parse_settings(self, filepath):
        with open(filepath, 'r') as f:
            settings = [line.split(':', 1) for line in f.readlines()]
            settings = map(lambda arr: [elem.strip() for elem in arr], settings)

            for setting in settings:
                match setting:
                    case ['']:
                        continue

                    case [name, ''] | [name]:
                        self.set_setting(name)

                    case [name, value]:
                        self.set_setting(name, value)