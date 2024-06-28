from consts import level_cost
import json

def reset():
  if input("Are you sure you want to reset all levels to 1? (y/n): ") != 'y':
    return
  for recipe in data:
     recipe['current_level'] = 1
  print("Levels reset to 1")

def get_recipe(name):
  for recipe in data:
    if recipe['recipe_name'].lower() == name.lower():
      format_recipe(recipe)
      return
  print("Recipe not found")
  
def format_recipe(recipe):
  recipe_string = f"\n{recipe['recipe_name']} (Level {recipe['current_level']})\n"
  for fish in recipe['fish']:
    recipe_string += f"{fish['fish_name']}: {fish['amount']}\n"
  print(recipe_string)

def calculate_all_amounts():
  amounts = {} 

  for recipe in data:
    for fish in recipe['fish']:
      fish_name = fish['fish_name']

      if fish_name not in amounts.keys():
        amounts[fish_name] = 0

      for level in range(recipe['current_level'] + 1, len(level_cost) - 1):
        fish_cost = fish['amount']

        match fish_cost:
          case 1:
            amounts[fish_name] += level_cost[level]

          case 2:
            amounts[fish_name] += level_cost[level + 1]

          case 3:
            amounts[fish_name] += level_cost[level] * 2 + (level % 2) # +1 if upgrading to odd level

          case 5:
            amounts[fish_name] += level_cost[level] * 3 + (level % 2) # +1 if upgrading to odd level

          case _:
            print(f"Invalid fish cost for {fish_name}")

  for fish in amounts:
    print(f"{fish}: {amounts[fish]}")

def calculate_amount():
  ...

def find_recipe_by_ingredient():
  ...

def find_recipe_by_name():
  ...

def upgrade_recipe():
  ...

def print_options():
    print("                   Options"                    )
    print("----------------------------------------------")
    print("1. Reset all levels to 1")
    print("2. Get recipe by name")
    print("3. Calculate all amounts")
    print("4. Calculate amount for a specific recipe")
    print("5. Find recipe by ingredient")
    print("6. Find recipe by name")
    print("7. Upgrade recipe")
    print("8. Exit\n")

def choice_to_func(choice):
    if choice == 1:
      reset()
    elif choice == 2:
      name = input("Enter recipe name: ")
      get_recipe(name)
    elif choice == 3:
      calculate_all_amounts()
    elif choice == 4:
      calculate_amount()
    elif choice == 5:
      find_recipe_by_ingredient()
    elif choice == 6:
      find_recipe_by_name()
    elif choice == 7:
      upgrade_recipe()
    elif choice == 8:
      return False
    else:
      print("Invalid choice. Please try again.")
    return True

if __name__ == "__main__":
  stay = True
  data = []
  with open('data.json') as f:
      data = json.load(f)
    
  while stay:
    print_options()
    choice = int(input("Enter your choice: "))
    result = choice_to_func(choice)
    if !(result):
        return
    cont = input("\nContinue? (y/n)")
    if cont.lower == 'n':
      stay = False


