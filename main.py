import ccxt
import time
from ccxt.base.errors import NetworkError, RequestTimeout
from datetime import datetime

market_place = ccxt.binance()
while True:
    try:
        ticker = market_place.fetch_ticker('XRP/USDT')
        current_price = ticker['last']

        max_price = max(current_price, ticker['high'])

        if max_price == 0:
            max_price = current_price
        else:
            if current_price < max_price * 0.99:
                print("Цена упала на 1% от максимальной цены::", max_price, "->", current_price)

        time.sleep(3600)

        print(f"Цена XRP/USDT: {ticker['last']}")
        with open('data.txt', 'w', encoding="UTF-8") as f:
            f.write(f"Цена упала на 1% от максимальной цены::, {max_price}, - {current_price}\n")


    except NetworkError as e:
        print("У вас нет подключения к интернету\n")
        time.sleep(5)
        print("пытаемся восстановить подключение.....")
        time.sleep(5)
        continue
    except KeyboardInterrupt as d:
        print("Ваша программа успешно закрылась")
        break
    except RequestTimeout as Timeout:
        print("Увы, ваше время вышло")
        break
