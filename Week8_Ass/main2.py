from Week8_Ass.lib.interface import *
from Week8_Ass.lib.archive import *
from time import sleep
import datetime as d

inventory = 'carsale.txt'
sold = 'carsold.txt'
allcars = 'allcars.txt'

inventory2 = 'sale.dat'
sold2 = 'sold.dat'
allcars2 = 'allcars.dat'

if not fileExists(inventory):
    createFile(inventory)
if not fileExists(sold):
    createFile(sold)
if not fileExists(allcars):
    createFile(allcars)
if not fileExists(inventory2):
    createFile(inventory2)
if not fileExists(sold2):
    createFile(sold2)
if not fileExists(allcars2):
    createFile(allcars2)

while True:
    asw = menu(['Inventory', 'Car Management', 'Calculator', 'Find a Car', 'Exit'])

    if asw == 1:
        while True:
            # Nested inventory
            asw = menu(['Available Cars', 'Sold Cars', 'All Cars', 'Back', 'Exit Program'])
            if asw == 1:
                # Show inventory
                readFile(inventory, 'INVENTORY')
            elif asw == 2:
                # Show sold cars
                readFile(sold, 'SOLD CARS')
            elif asw == 3:
                # Show all cars (purchased and sold)
                readFile(allcars, 'ALL CARS')
            elif asw == 4:
                # Go back to main menu
                break
            elif asw == 5:
                # Exit program
                title('Exiting... See you later!')
                exit()
            else:
                print('\033[31mError! Enter a valid option.\033[m')
            sleep(.5)
    elif asw == 2:
        while True:
            # Car management
            asw = menu(['Add New Car', 'Sell Car', 'Remove From Files', 'Back', 'Exit Program'])
            if asw == 1:
                # Add new car
                x = 'yes'
                while x.lower() == 'yes':
                    title('ADD NEW CAR')
                    make = str(input('Make: '))
                    model = str(input('Model: '))
                    chassis = str(input('Chassis: '))
                    pur_price = int(input('Purchased price: '))
                    pur_year = int(input('Purchased year: '))
                    pur_month = int(input('Purchased month: '))
                    pur_day = int(input('Purchased day: '))
                    # getPur_Date(pur_year, pur_month, pur_day)
                    add(inventory, 'NEW CAR ADDED', make, model, chassis, pur_price,
                        getPur_Date(pur_year, pur_month, pur_day))
                    add(allcars, '', make, model, chassis, pur_price,
                        getPur_Date(pur_year, pur_month, pur_day))
                    x = str(input('Do you want to add another car? (yes or no): '))
            elif asw == 2:
                # Sell a car
                x = 'yes'
                while x.lower() == 'yes':
                    title('SELLING')
                    chassis = str(input('Chassis: '))
                    remove(allcars, chassis)
                    sold_price = int(input('Sold Price: '))
                    sold_year = int(input('Sold year: '))
                    sold_month = int(input('Sold month: '))
                    sold_day = int(input('Sold day: '))
                    sell(chassis, sold_price, d.date(sold_year, sold_month, sold_day))
                    remove(inventory, chassis)
                    x = str(input('Do you want to sell another car? (yes or no): '))
            elif asw == 3:
                # Remove Car
                x = 'yes'
                while x.lower() == 'yes':
                    title('REMOVE')
                    chassis = str(
                        input('Enter the chassis of the car you want to remove (Cars removed will be lost forever): '))
                    remove(inventory, chassis)
                    remove(sold, chassis)
                    remove(allcars, chassis)
                    x = str(input('Do you want to remove another car? (yes or no): '))
            elif asw == 4:
                # Go back to main menu
                break
            elif asw == 5:
                # Exit program
                title('Exiting... See you later!')
                exit()
            else:
                print('\033[31mError! Enter a valid option.\033[m')
            sleep(.5)
    elif asw == 3:
        while True:
            # Show calculation menu
            asw = menu(['Spent', 'Sales', 'Benefit', 'Back', 'Exit Program'])
            if asw == 1:
                while True:
                    asw = menu(['By year', 'By Make', 'By model', 'Back', 'Exit Program'])
                    if asw == 1:
                        # Calculate the total spent over a range of years
                        x = 'yes'
                        while x.lower() == 'yes':
                            title('TOTAL SPENT (YEAR)')
                            print(
                                'To calculate the total spent in a range of years enter the start and end year bellow:')
                            start_year = int(input('Start year: '))
                            end_year = int(input('End year: '))
                            print(f'The total spent between {start_year} and {end_year} '
                                  f'was ${calcSpent(allcars, start_year, end_year)}')
                            x = str(input('Do you want to calculate the spent in other years? (yes or no): '))
                    elif asw == 2:
                        # Calculate the total spent of a specific make
                        x = 'yes'
                        while x.lower() == 'yes':
                            title('TOTAL SPENT (MAKE)')
                            make = input('Make: ')
                            print(f'The total spent for {make} '
                                  f'was ${calcSpentMake(allcars, make)}')
                            x = str(input('Do you want to calculate the spent for other make? (yes or no): '))
                    elif asw == 3:
                        # Calculate the total spent of a specific model
                        x = 'yes'
                        while x.lower() == 'yes':
                            title('TOTAL SPENT (MODEL)')
                            model = input('Model: ')
                            print(f'The total spent for {model} '
                                  f'was ${calcSpentModel(allcars, model)}')
                            x = str(input('Do you want to calculate the spent for other model? (yes or no): '))
                    elif asw == 4:
                        # Go back to the previous menu
                        break
                    elif asw == 5:
                        # Exit program
                        title('Exiting... See you later!')
                        exit()
                    else:
                        print('\033[31mError! Enter a valid option.\033[m')
                    sleep(.5)
            elif asw == 2:
                while True:
                    asw = menu(['By year', 'By Make', 'By model', 'Back', 'Exit Program'])
                    if asw == 1:
                        # Calculate the total sales over a range of years
                        x = 'yes'
                        while x.lower() == 'yes':
                            title('TOTAL SALES')
                            print(
                                'To calculate the total sales in a range of years enter the start and end year bellow:')
                            start_year = int(input('Start year: '))
                            end_year = int(input('End year: '))
                            print(
                                f'The total sales between {start_year} and {end_year} was ${calcSales(sold, start_year, end_year)}')
                            x = str(input('Do you want to calculate the spent in other year? (yes or no): '))
                    elif asw == 2:
                        # Calculate the total sales of a specific make
                        x = 'yes'
                        while x.lower() == 'yes':
                            title('TOTAL SALES (MAKE)')
                            make = input('Make: ')
                            print(f'The total sales for {make} '
                                  f'was ${calcSalesMake(sold, make)}')
                            x = str(input('Do you want to calculate the sales for other make? (yes or no): '))
                    elif asw == 3:
                        # Calculate the total sales of a specific model
                        x = 'yes'
                        while x.lower() == 'yes':
                            title('TOTAL SALES (MODEL)')
                            model = input('Model: ')
                            print(f'The total sales for {model} '
                                  f'was ${calcSalesModel(sold, model)}')
                            x = str(input('Do you want to calculate the sales for other model? (yes or no): '))
                    elif asw == 4:
                        # Go back to the previous menu
                        break
                    elif asw == 5:
                        # Exit program
                        title('Exiting... See you later!')
                        exit()
                    else:
                        print('\033[31mError! Enter a valid option.\033[m')
                    sleep(.5)
            elif asw == 3:
                while True:
                    asw = menu(['By year', 'By Make', 'By model', 'Back', 'Exit Program'])
                    if asw == 1:
                        # Calculate the total benefit over a range of years
                        x = 'yes'
                        while x.lower() == 'yes':
                            title('BENEFIT (YEAR)')
                            print('To calculate the benefit in a range of years enter the start and end year bellow:')
                            start_year = int(input('Start year: '))
                            end_year = int(input('End year: '))
                            benefit = calcBenefit(allcars, sold, start_year, end_year)
                            if benefit < 0:
                                print(f'The benefit between {start_year} and {end_year} was $\033[31m{benefit}\033[m.')
                            elif benefit > 0:
                                print(f'The benefit between {start_year} and {end_year} was $\033[32m{benefit}\033[m.')
                            else:
                                print(f'The benefit between {start_year} and {end_year} was $0.')
                            x = str(input('Do you want to calculate the benefit in other year? (yes or no): '))
                    elif asw == 2:
                        # Calculate the benefit of a specific make
                        x = 'yes'
                        while x.lower() == 'yes':
                            title('BENEFIT (MAKE)')
                            make = input('Make: ')
                            benefit = calcBenefitMake(allcars, sold, make)
                            if benefit < 0:
                                print(f'The benefit for {make} was $\033[31m{benefit}\033[m.')
                            elif benefit > 0:
                                print(f'The benefit for {make} was $\033[32m{benefit}\033[m.')
                            else:
                                print(f'The benefit for {make} was $0.')
                            x = str(input('Do you want to calculate the benefit for other make? (yes or no): '))
                    elif asw == 3:
                        # Calculate the benefit of a specific model
                        x = 'yes'
                        while x.lower() == 'yes':
                            title('BENEFIT (MODEL)')
                            model = input('Model: ')
                            benefit = calcBenefitModel(allcars, sold, model)
                            if benefit < 0:
                                print(f'The benefit for {model} was $\033[31m{benefit}\033[m.')
                            elif benefit > 0:
                                print(f'The benefit for {model} was $\033[32m{benefit}\033[m.')
                            else:
                                print(f'The benefit for {model} was $0.')
                            x = str(input('Do you want to calculate the benefit for other model? (yes or no): '))
                    elif asw == 4:
                        # Go back to the previous menu
                        break
                    elif asw == 5:
                        # Exit program
                        title('Exiting... See you later!')
                        exit()
                    else:
                        print('\033[31mError! Enter a valid option.\033[m')
                    sleep(.5)
            elif asw == 4:
                # Go back to main menu
                break
            elif asw == 5:
                # Exit program
                title('Exiting... See you later!')
                exit()
            else:
                print('\033[31mError! Enter a valid option.\033[m')
            sleep(.5)
    elif asw == 4:
        # Find a car
        while True:
            asw = menu(['By year', 'By Make', 'By model', 'Back', 'Exit Program'])
            if asw == 1:
                # Find car by year
                title('FIND CAR (YEAR)')
                print('To find the cars in a range of years enter the start and end year bellow:')
                start_year = int(input('Start year: '))
                end_year = int(input('End year: '))
                findCar(allcars, start_year, end_year)
            elif asw == 2:
                # Find car by make
                title('FIND CAR (MAKE)')
                print('To find the cars of a make enter the make bellow:')
                make = input('Make: ')
                findCarMake(allcars, make)
            elif asw == 3:
                # Find car by model
                title('FIND CAR (MODEL)')
                print('To find the cars of a model enter the model bellow:')
                model = input('Model: ')
                findCarModel(allcars, model)
            elif asw == 4:
                # Back to previous menu
                break
            elif asw == 5:
                # Exit program
                exit()
            else:
                print('\033[31mError! Enter a valid option.\033[m')
    elif asw == 5:
        # Exit
        title('Exiting... See you later!')
        break
    else:
        print('\033[31mError! Enter a valid option.\033[m')
    sleep(.5)
