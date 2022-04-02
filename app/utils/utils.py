from datetime import datetime

def str2time(value):
    try:
        return datetime.strptime(value, '%H:%M')
    except Exception as err:
        return str(err)