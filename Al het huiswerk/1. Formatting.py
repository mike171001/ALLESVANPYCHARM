
def convert(fahrenheit):
    return (fahrenheit * 1.8) + 32

def table():
    print('{0:5}\t{1:5}'.format('   C  ', '   F  '))
    for i in range(-30, 50, 10):
        print('{0:5}\t{1:5}'.format(convert(i), i))


table()

