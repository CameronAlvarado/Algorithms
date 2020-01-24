#!/usr/bin/python

# import argparse

# def find_max_profit(prices):

# 	# keep track of the currest smallest price so far
# 	cur_min_price = 0

# 	# keep track of the currest largest price so far
# 	cur_max_price = 0

# 	# keep track of the max profit so far.
# 	cur_max_profit = 0

# 	# array that ranges from beginning of list to the cur_max_price's index
# 	temp_arr = prices

# 	# keep track of index of current max price in prices
# 	max_price_index = 0

# 	# Find the maximum difference between the smallest and largest prices in the list.
# 	for x in prices:
# 		if x < 1:
# 			pass
# 		elif x > cur_max_price:
# 			cur_max_price = x
# 			print("cur max price:", cur_max_price)
# 			max_price_index = prices.index(cur_max_price)
# 			temp_arr = prices[:max_price_index + 1]
# 			print("temp arr:", temp_arr)
# 			for x in temp_arr:
# 				if cur_min_price == 0:
# 					cur_min_price = x
# 					print("cur min price 1:", cur_min_price)
# 				elif x < cur_min_price:
# 					cur_min_price = x
# 					print("cur min price 2:", cur_min_price)
# 				if max_price_index == 1 :
# 					cur_max_profit = prices[max_price_index + 1] - prices[max_price_index]
# 					print("this one")
# 					return cur_max_profit
# 				else:
# 					cur_max_profit = prices[max_price_index] - cur_min_price
# 					print("that one")
# 					return cur_max_profit

def find_max_profit(prices):
  # find max value
  max_index = prices.index(max(prices)) # finding index of the max value in list
  if max_index == 0: 
    new_arr_minus_max = prices[1:] # making a new list if the maximum value is in index[0]
    max_index_new = max(new_arr_minus_max) # max of new list (new_arr_minus_max)
    if max_index_new is new_arr_minus_max[0]: # if that new max is in index[0] of new array
      return (max_index_new - max(prices)) # new list max - the max of the old list
    else: 
      return (max(new_arr_minus_max) - min(new_arr_minus_max)) # new list max - new list min
  else:
    # split the array left and right (where the biggest value is)
    new_arr = prices[0:max_index + 1]
    return (max(new_arr) - min(new_arr))




if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))