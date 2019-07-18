#!/usr/bin/python

import argparse

def find_max_profit(prices):
  buy_price = 0
  sell_price = 0

  for i in range(len(prices)-1):
    i_index = i
    for j in range(i + 1, len(prices)-1):
      if prices[i+1] > prices[i_index]:
        buy_price = prices[i_index]
        sell_price = prices[j]
        difference = sell_price - buy_price
        if prices[i+1] < buy_price:
          prices[i+1] = buy_price
        j += 1        
        return difference


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))