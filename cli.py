import interactive as i
from data_module import data as d
import util as u

choice_mapper = [
  {
    "text": "Get Recipe by Name",
    "function": i.get_recipe
  },
  {
    "text": "Get Recipe by Ingredient",
    "function": i.get_recipe_from_ingredient
  },
  {
    "text": "Calculate Amounts",
    "function": i.calculate_amounts,
    "options": [
      {
        "text": "All Ingredients",
        "key": "no_arg"
      },
      {
        "text": "Ingredient",
        "key": "ingredient",
        "type": "fuzzy_ingredient"
      },
      {
        "text": "Recipe",
        "key": "function",
        "function": i.calculate_recipe
      },
      {
        "text": "Category",
        "key": "category",
        "type": "select",
        "options": ["Seafood", "Plants", "Seasoning"]
      },
      {
        "text": "Number of Ingredients",
        "key": "num_ingredients",
        "type": "number",
        "max": 12
      }
    ]
  },
  {
    "text": "Upgrade Recipe",
    "function": i.upgrade_recipe
  },
  {
    "text": "Continuously Upgrade Recipes",
    "function": i.continuous_upgrade
  },
  {
    "text": "Backup Data",
    "function": d.create_backup
  },
  {
    "text": "Restore Backup",
    "function": d.restore_backup
  },
  {
    "text": "Reset All Data",
    "function": i.reset
  },
  {
    "text": "Exit"
  }
]

def print_options(options):
  print()
  for option in options:
    print(f"{options.index(option) + 1}: {option['text']}")


if __name__ == "__main__":
  first_run = True
  while True:
    if not first_run:
      input("Press Enter to continue...")
    first_run = False

    print_options(choice_mapper)
    choice = input(f"Enter choice 1-{len(choice_mapper)}: ")
    print()
    
    try:
      selection = choice_mapper[int(choice.strip()) - 1]
    
      if not selection:
        print("Invalid choice")
        print()
        continue

      if not callable(selection.get('function')):
        print("Exiting...")
        break

      if not selection.get('options'):
        selection['function']()
        continue

      print_options(selection['options'])
      option_choice = int(input("Enter choice: ").strip()) - 1

      option = selection['options'][option_choice]
      key = option['key']

      if key == "no_arg":
        selection['function']()
        continue

      if key == "function":
        option['function']()
        continue


      match option['type']:
        case "fuzzy_ingredient":
          argument = u.fuzzy_find_ingredients(input("Enter ingredient: ").strip())

        case "number":
          argument = int(input("Enter number: "))

        case "select":
          nested_option = u.choice_picker("Which option?", option['options'])
          print()
          argument = option['options'][nested_option]
        
        case _:
          continue

      selection['function']({key: argument})

    except (ValueError, IndexError):
      print("Invalid choice")
