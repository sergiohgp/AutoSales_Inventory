from Week8_Ass.lib.interface import *
from time import sleep
import datetime as d


def fileExists(name):
    try:
        f = open(name, 'rt')
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(name):
    try:
        f = open(name, 'wt+')
        f.close()
    except:
        print('Error when try to create the file!')
    else:
        print(f'{name} was created!')


def readFile(name, t):
    try:
        f = open(name, 'rt')
    except:
        print('Read file error.')
    else:
        title(t)
        m = 'Make'
        mo = 'Model'
        p = 'Payed Price'
        pd = 'Purchased Date'
        sd = 'Sold Date'
        ch = 'Chassis'
        sp = 'Sold Price'
        print(f'\033[36m{m:<15}{mo:<14}{ch:<14}{p:<16}{pd:<22}{sp:<16}{sd:>15}\033[m')
        for line in f:
            datum = line.split(' ')
            datum[6] = datum[6].replace('\n', '')
            print(f'{datum[0]:<15}{datum[1]:<15}{datum[2]:<15}${datum[3]:<15}'
                  f'{datum[4]:<21}${datum[5]:<14}{datum[6]:>15}')
            # sleep(.3)

    finally:
        f.close()


def readLine(line):
    datum = line.split()
    datum[6] = datum[6].replace('\n', '')
    print(f'{datum[0]:<15}{datum[1]:<15}{datum[2]:<15}${datum[3]:<15}'
          f'{datum[4]:<21}${datum[5]:<14}{datum[6]:>15}')


def add(file, msg, make, model, chassis, pur_price=0, pur_date='Unknown', sold_price='-', sold_date='-'):
    try:
        f = open(file, 'at')
    except:
        print('There was an error in the opening.')
    else:
        try:
            f.write(f'{make} {model} {chassis} {pur_price} {pur_date} {sold_price} {sold_date}\n')
        except:
            print('Error writing data.')
        else:
            print(msg)
            f.close()


def remove(file, chassis):
    try:
        f = open(file, 'r+')
    except:
        print('There was an error trying to read.')
    else:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if chassis not in line:
                f.write(line)
        f.truncate()
        f.close()


def sell(chassis, sold_price, sold_date):
    f = open("carsale.txt", "rt")
    ff = open('carsold.txt', 'at')
    fff = open('allcars.txt', 'at')
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
        if chassis in line:
            line = line.split()
            line[5] = line[5].replace('-', str(sold_price))
            line[6] = line[6].replace('-', str(sold_date))
            line = str(line)
            line = line.replace('[', '')
            line = line.replace("'", '')
            line = line.replace(',', '')
            line = line.replace(']', '')
            ff.write(line)
            fff.write(line)
    f.close()
    ff.close()
    fff.close()


def calcSpent(file, start_year, end_year):
    try:
        f = open(file, 'rt')
    except:
        print('There was an error trying to read.')
    else:
        new_f = f.readlines()
        f.seek(0)
        t = 0
        for line in new_f:
            array = line.split()
            array2 = array[4].split('-')
            for year in range(start_year, end_year + 1):
                if str(year) == array2[0]:
                    pur = int(array[3].replace('$', ''))
                    t += pur
        f.close()
        return t


def calcSpentMake(file, make):
    try:
        f = open(file, 'rt')
    except:
        print('There was an error trying to read.')
    else:
        new_f = f.readlines()
        f.seek(0)
        t = 0
        for line in new_f:
            array = line.split()
            if str(make) == array[0]:
                pur = int(array[3].replace('$', ''))
                t += pur
        f.close()
        return t


def calcSpentModel(file, model):
    try:
        f = open(file, 'rt')
    except:
        print('There was an error trying to read.')
    else:
        new_f = f.readlines()
        f.seek(0)
        t = 0
        for line in new_f:
            array = line.split()
            if str(model) == array[1]:
                pur = int(array[3].replace('$', ''))
                t += pur
        f.close()
        return t


def calcSales(file, start_year, end_year):
    try:
        f = open(file, 'rt')
    except:
        print('There was an error trying to read.')
    else:
        new_f = f.readlines()
        f.seek(0)
        t = 0
        for line in new_f:
            array = line.split()
            array2 = array[6].split('-')
            for year in range(start_year, end_year + 1):
                if str(year) == array2[0]:
                    pur = int(array[5].replace('$', ''))
                    t += pur
        f.close()
        return t


def calcSalesMake(file, make):
    try:
        f = open(file, 'rt')
    except:
        print('There was an error trying to read.')
    else:
        new_f = f.readlines()
        f.seek(0)
        t = 0
        for line in new_f:
            array = line.split()
            if str(make) == array[0]:
                pur = int(array[5].replace('$', ''))
                t += pur
        f.close()
        return t


def calcSalesModel(file, model):
    try:
        f = open(file, 'rt')
    except:
        print('There was an error trying to read.')
    else:
        new_f = f.readlines()
        f.seek(0)
        t = 0
        for line in new_f:
            array = line.split()
            if str(model) == array[1]:
                pur = int(array[5].replace('$', ''))
                t += pur
        f.close()
        return t


def calcBenefit(file1, file2, start_year, end_year):
    try:
        f = open(file1, 'rt')
        ff = open(file2, 'rt')
    except:
        print(f'There was an error trying to open {file1} or {file2}.')
    else:
        benefit = int(calcSales(file2, start_year, end_year)) - int(calcSpent(file1, start_year, end_year))
        f.close()
        ff.close()
        return benefit


def calcBenefitMake(file1, file2, make):
    try:
        f = open(file1, 'rt')
        ff = open(file2, 'rt')
    except:
        print(f'There was an error trying to open {file1} or {file2}.')
    else:
        benefit = int(calcSalesMake(file2, make)) - int(calcSpentMake(file1, make))
        f.close()
        ff.close()
        return benefit


def calcBenefitModel(file1, file2, model):
    try:
        f = open(file1, 'rt')
        ff = open(file2, 'rt')
    except:
        print(f'There was an error trying to open {file1} or {file2}.')
    else:
        benefit = int(calcSalesModel(file2, model)) - int(calcSpentModel(file1, model))
        f.close()
        ff.close()
        return benefit


def getPur_Date(pur_year, pur_month, pur_day):
    pur_date = d.date(pur_year, pur_month, pur_day)
    return pur_date


def findCar(file, start_year, end_year):
    try:
        f = open(file, 'rt')

    except:
        print(f'There was an error trying to open {file}.')
    else:
        title(f'ALL CARS BETWEEN {start_year} AND {end_year}')
        m = 'Make'
        mo = 'Model'
        p = 'Payed Price'
        pd = 'Purchased Date'
        sd = 'Sold Date'
        ch = 'Chassis'
        sp = 'Sold Price'
        print(f'\033[36m{m:<15}{mo:<14}{ch:<14}{p:<16}\033[m\033[31m{pd:<22}\033[m\033[36m{sp:<16}{sd:>15}\033[m')
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            array = line.split()
            array2 = array[4].split('-')
            for year in range(start_year, end_year + 1):
                if str(year) == array2[0]:
                    readLine(line)
        f.close()


def findCarMake(file, make):
    try:
        f = open(file, 'rt')

    except:
        print(f'There was an error trying to open {file}.')
    else:
        title(f'ALL CARS OF {make.upper()}.')
        m = 'Make'
        mo = 'Model'
        p = 'Payed Price'
        pd = 'Purchased Date'
        sd = 'Sold Date'
        ch = 'Chassis'
        sp = 'Sold Price'
        print(f'\033[31m{m:<15}\033[m\033[36m{mo:<14}{ch:<14}{p:<16}{pd:<22}{sp:<16}{sd:>15}\033[m')
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            array = line.split()
            if make == array[0]:
                readLine(line)
        f.close()


def findCarModel(file, model):
    try:
        f = open(file, 'rt')

    except:
        print(f'There was an error trying to open {file}.')
    else:
        title(f'ALL CARS OF {model.upper()}.')
        m = 'Make'
        mo = 'Model'
        p = 'Payed Price'
        pd = 'Purchased Date'
        sd = 'Sold Date'
        ch = 'Chassis'
        sp = 'Sold Price'
        print(f'\033[36m{m:<15}\033[m\033[31m{mo:<14}\033[36m{ch:<14}{p:<16}{pd:<22}{sp:<16}{sd:>15}\033[m')
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            array = line.split()
            if model == array[1]:
                readLine(line)
        f.close()
