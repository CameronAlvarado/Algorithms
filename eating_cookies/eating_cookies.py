# #!/usr/bin/python

# import sys

# # The cache parameter is here for if you want to implement
# # a solution that is more efficient than the naive 
# # recursive solution
# def eating_cookies(n, cache=None):
# 	if cache is None:
# 		cache = {0: 1, 1: 1, 2: 2}
# 	if n < 0:
# 		return 0
# 	elif n not in cache:
# 		cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
# 	return cache[n]

# # print(eating_cookies(3))

import datetime

start = datetime.datetime.now()

# def eating_cookies(n, cache=None):
# 	if n < 0:
# 		return 0
# 	elif n == 0:
# 		return 1
# 	else:
# 		result = eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
# 		end = datetime.datetime.now()
# 		total = end - start
# 		print(total)

# 		return result

# print(eating_cookies(10))

def eating_cookies(n, cache=None):
	if cache is None or type(cache) == list:
		cache = {0:1, 1:1, 2:2, 3:4}
	if n < 0:
		return 0
	elif n not in cache:
		cache[n] = eating_cookies(n - 3, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 1, cache)
		end = datetime.datetime.now()
		total = end - start
		print(total)
	return cache[n]

print(eating_cookies(10))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')