from datetime import datetime

def get_days_from_today(date):

    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        today_date = datetime.today()
        days_delta = (today_date - input_date).days
        return days_delta
    except ValueError:
        print('Incorrect date format. Use the YYYY-MM-DD format')