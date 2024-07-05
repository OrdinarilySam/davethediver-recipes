import interactive as i
from data_module import data as d

"""
reset
get_recipe
get_recipe_from_ingredient
calculate_amounts
  name->use fuzzy find
  category->[seafood, plants, seasoning]
  filters->[sushi, recipe]
upgrade_recipe
continuous_upgrade
calculate_recipe


"""

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
        "text": "Name",
        "key": "name",
        "type": "fuzzy_ingredient"
      },
      {
        "text": "Recipe",
        "key": None,
        "function": i.calculate_recipe
      },
      {
        "text": "Category",
        "key": "category",
        "type": "select",
        "options": ["Seafood", "Plants", "Seasoning"]
      },
      {
        "text": "Filter",
        "key": "filter",
        "type": "select",
        "options": ["Sushi", "Recipe"]
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

def print_options():
  ...


if __name__ == "__main__":
  while True:
    print_options(choice_mapper)
    choice = input("Enter choice: ")
    
    try:
      selection = choice_mapper[int(choice.strip()) + 1]
    except (ValueError, IndexError):
      selection = None

    if not selection:
      print("Invalid choice")
      print()
      continue

    if callable(selection.get('function')):
      if not selection.get('options'):
        selection['function']()
      else:
        print_options(selection)

    else:
      print("Exiting...")
      break