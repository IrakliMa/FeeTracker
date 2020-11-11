import requests
import csv
import time

# Get Ethereum price in USD from CoinGecko
request_price = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
price = request_price.json()['ethereum']['usd']

# Get gas data from EthGasStation
request_data = requests.get('https://ethgasstation.info/api/ethgasAPI.json?api-key=10e6255a2d0d44851f2cea620e804b477fba1a13253909141b3f7b40024c')
data = request_data.json()

# with open('fees.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Ethereum:", price])
#     writer.writerow(["Fast Gwei", "Fast Mins", "Fast tx USD", "Fast erc tx USD"])

# In Gwei
fast_gwei = data['fast']/10
average_gwei = data['average']/10
slow_gwei = data['safeLow']/10

# Eth tx In USD
#WTF? 21000000 != 1000000 * 21?
fast_fee = round(fast_gwei * price / 1000000 * 21, 2) 
average_fee = round(average_gwei * price / 1000000 * 21, 2)
slow_fee = round(slow_gwei * price / 1000000 * 21, 2)

# Erc20 tx In USD
erc20_fast_fee = round(fast_gwei * price / 1000000 * 80, 2) 
erc20_average_fee = round(average_gwei * price / 1000000 * 80, 2)
erc20_slow_fee = round(slow_gwei * price / 1000000 * 80, 2)


# In Mins
fast_time = data['fastWait']
average_time = data['avgWait']
slow_time = data['safeLowWait']

print(fast_gwei, fast_time, fast_fee, erc20_fast_fee)
with open('fees.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Ethereum:", price])
    writer.writerow(["Fast Gwei", "Fast Mins", "Fast tx USD", "Fast erc tx USD"])

    while(True):
      writer.writerow([fast_gwei, fast_time, fast_fee, erc20_fast_fee])
      time.sleep(6)
