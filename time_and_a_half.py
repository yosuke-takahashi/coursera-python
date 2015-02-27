hrs = float(raw_input('Enter Hours: '))
rate = float(raw_input('Enter Rate: '))


def computepay(hrs, rate):
    if hrs > 40.0:
        diff = hrs - 40.0
        print hrs * rate + diff * rate/2


pay = computepay(hrs, rate)
