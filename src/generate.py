import datetime as dtime
import random as rnd

import settings as st
import data as dt
import reports as rp

settings_file = 'settings.txt'

def generate_doc(settings):
    data = dt.Data()

    with open(settings.output_file, 'w', encoding='utf-8') as f:
        time = settings.start_time
        n = settings.n_reports
        for i in range(n):
            min_offset = rnd.randint(5, 120)
            sec_offset = rnd.randint(0, 59)
            time += dtime.timedelta(minutes=min_offset, seconds=sec_offset)
            timestamp = time.ctime()

            report = rnd.choice(rp.reports)
            f.write(report(timestamp, data) + '\n')

            if i != n - 1:
                f.write('=' * 80 + '\n')

            time += dtime.timedelta(days=1)

            if (i % (n // 10) == 0 and i != 0):
                print(f'    {i // (n // 10) * 10}%')

        print(f'[{settings.output_file}]: Выходной файл готов!')


if __name__ == '__main__':
    settings = st.Settings()

    print(f'[{settings_file}]: Чтениe настроек...') 
    settings.parse_settings(settings_file)

    print(f'[{settings.output_file}]: Генераця выходного файла...')
    generate_doc(settings)
        
