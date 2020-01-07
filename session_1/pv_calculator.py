# Simple CLI

future_value = int(input('Enter the desired future value: '))

rate = float(input('Enter the annual interest rate: '))

years = int(input('Enter the number of years the money will grou: '))

presnet_value = future_value / (1.0 + rate) ** years

print(f'You will need to deposit this amount: {presnet_value}!')
