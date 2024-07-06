from data_module.data import data, maxed_list, save_data, ingredients


# added extra 0 at start for easier indexing in calculate amounts
level_cost = [0,0,3,4,6,10,15,22,34,51,76,115]


def format_recipe(recipe):
  recipe_string = f"\n{recipe['recipe_name']} (Level {recipe['current_level']})\n"
  for fish in recipe['fish']:
    recipe_string += f"{fish['fish_name']}: {fish['amount']}\n"
  print(recipe_string)


def fuzzy_find_ingredients(search):
  all_ingredients = set(
    [fish for category in ingredients for fish in ingredients[category]]
  )
  found = []

  for ingredient in all_ingredients:
    if search.lower() in ingredient.lower():
      found.append(ingredient)
  return found


def fuzzy_find_recipe(search):
  found = []
  for recipe in data:
    if search.lower() in recipe['recipe_name'].lower():
      found.append(recipe)
  return found

def format_ingredients(ingredients):
  done = []
  still_needed = []

  for fish in ingredients:
    if not ingredients[fish]:
      done.append(fish)
    else:
      still_needed.append(fish)
    
  print("Done:")
  for fish in done:
    print(fish)
  print()

  if not len(still_needed):
    return
  longest_fish_name = max([len(fish) for fish in still_needed])

  print("Still Needed:")
  for fish in still_needed:
    print(f"{fish:>{longest_fish_name}}: {str(ingredients[fish])}")
  print()

def calculate_cost(recipe):
  costs = {}
  for fish in recipe['fish']:
    fish_name = fish['fish_name']
    fish_cost = fish['amount']

    costs[fish_name] = 0

    for level in range(recipe['current_level'] + 1, recipe['max_level'] + 1):
      fish_cost = fish['amount']

      match fish_cost:
        case 1:
          costs[fish_name] += level_cost[level]

        case 2:
          costs[fish_name] += level_cost[level + 1]

        case 3:
          costs[fish_name] += level_cost[level] * 2 + (level % 2) # +1 if upgrading to odd level

        case 5:
          costs[fish_name] += level_cost[level] * 3 + (level % 2) # +1 if upgrading to odd level

        case _:
          print("Invalid fish cost for " + fish_name)

  return costs


def add_max_level():
  for recipe in data:
    recipe['max_level'] = 10 if recipe['recipe_name'] not in maxed_list else 1
  save_data()


def choice_picker(text, options):
  if not len(options):
    return None
  
  if len(options) > 1:
    for index, option in enumerate(options):
      print(index + 1, end=": ")
      print(option)
    
    print(text)

    while True:
      try:
        choice = int(input(f'Enter choice 1-{len(options)}: ').strip())
        if choice < 1 or choice > len(options):
          raise ValueError
        break

      except ValueError:
        print("Invalid choice")

    return choice - 1

  else:
    return 0
