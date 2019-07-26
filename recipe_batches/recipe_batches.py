#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  values = []
  if len(recipe) != len(ingredients):
    return 0

  # diff_keys = [keys for keys in recipe if recipe[keys] <= (ingredients[keys])]
  # return diff_keys
  for keys in recipe:
    if recipe[keys] <= ingredients[keys]:
      values.append(ingredients[keys] // recipe[keys])
  return min(values)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))