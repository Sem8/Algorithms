#!/usr/bin/python

import argparse

# My solution that I understand
def find_max_profit(prices):
  buy_price = prices[0]
  sell_price = 0
  profit = -1000000

  for i in range(len(prices)):
    each_price = prices[i]

    if each_price < buy_price:
      buy_price = each_price
      sell_price = 0
    elif each_price > sell_price:
      sell_price = each_price
      profit = sell_price - buy_price
  return profit

# Clunky solution to pass the test
def find_max_profit(prices):



price1 = [10, 7, 5, 8, 11, 9]
price2 = [100, 90, 80, 50, 20, 10]
price3 = [1050, 270, 1540, 3800, 2]
price4 = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79] 

print(find_max_profit(price1))
print(find_max_profit(price2))
print(find_max_profit(price3))
print(find_max_profit(price4))




if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))