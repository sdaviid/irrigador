from datetime import datetime

def str2time(value):
    try:
        return datetime.strptime(value, '%H:%M')
    except Exception as err:
        return str(err)


def str2date(value):
    try:
        return datetime.strptime(value, '%Y-%m-%d')
    except Exception as err:
        return str(err)