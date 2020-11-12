import requests
import csv
import time
import datetime

with open('fees.csv', 'w') as csvfile: # this will overwrite the already existing file
  writer = csv.writer(csvfile)

  # Write column titles
  writer.writerow(["Time", "ETH Price", "Fast Gwei", "Average Gwei", "Slow Gwei", "Fast Mins", "Average Mins", "Slow Mins", "Fast tx USD", "Average tx USD", "Slow tx USD", "Fast erc tx USD", "Average erc tx USD", "Slow erc tx USD"])

while(True):
  # Get Ethereum price in USD from CoinGecko
  request_price = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
  price = request_price.json()['ethereum']['usd']

  # Get gas data from EthGasStation
  request_data = requests.get('https://ethgasstation.info/api/ethgasAPI.json?api-key=workswitheverything')
  data = request_data.json()

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

  date = datetime.datetime.today()

  with open('fees.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow([date, price, fast_gwei, average_gwei, slow_gwei, fast_time, average_time, slow_time, fast_fee, average_fee, slow_fee, erc20_fast_fee,  erc20_average_fee, erc20_slow_fee])
  
  # Updates every 5 Mins
  time.sleep(300)