from datetime import datetime, timedelta
dt_now = datetime.now()
print(f"Сейчас {dt_now.strftime('%d.%m.%Y %H:%M')}")
delta = timedelta(days=1)
dt_yesterday = dt_now - delta
print(f'Вчера {dt_yesterday.strftime("%d.%m.%Y %H:%M")}')
delta = timedelta(days=30)
dt_month_ago = dt_now - delta
print(f'Примерно месяц назад {dt_month_ago.strftime("%d.%m.%Y %H:%M")}')

date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)
