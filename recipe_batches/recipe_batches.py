#!/usr/bin/python

import math

# This is mine:

# def recipe_batches(recipe, ingredients):
# 	# if ingredient ammounts are LESS than those in the recipie ammounts, return 0
# 	if len(ingredients) < len(recipe):
# 		return 0

# 	# if ingredient ammounts are EQUAL TO or MORE, do division
# 	else:
# 		recipe_vals = []
# 		ingredient_vals = []

# 		for item in recipe:
# 			recipe_vals.append(recipe[item])

# 		for item in ingredients:
# 			ingredient_vals.append(ingredients[item])

# 		for x in recipe_vals:
# 			for y in ingredient_vals:
# 				z = y // x
# 				return z

# This is Blake's

def recipe_batches(recipe, ingredients):
  # recipe is what is need 
  # ingredients is what we have 
  total_batches = []
  if set(ingredients) >= set(recipe):
    for x in recipe:
      # if we don't have enough of an ingredient, add 0 to list
      if recipe.get(x) > ingredients.get(x):
        total_batches.append(0)
      else:
        # if we have more than the recipe, divide evenly total batches made
        total_batches.append((ingredients[x] // recipe[x]))
    return min(total_batches)
  # if we have less than the recipe, return 0
  else:
    return 0

# recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }), 0
# recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 }), 1
# recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }), 2
# recipe_batches({ 'milk': 2 }, { 'milk': 200}), 100


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))