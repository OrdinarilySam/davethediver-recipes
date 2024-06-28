# Dave the Diver Recipes
Use this repo to figure out how many fish you need to max out your recipes in Dave the Diver.

**Requirements**:
- Python 3.10+

**Usage**:
1. Clone the repo
```
git clone https://github.com/OrdinarilySam/davethediver-recipes.git
cd davethediver-recipes
```

2. Create your own data file
```
cp data.json.template data.json
```

3. Run the python file in interactive mode (CLI coming soon)
```
python3 -i interactive.py
```

**Available Functions**:
optionally include a name to search for a recipe, leaving blank will return all recipes
- `calculate_amounts(name=None)`: Calculate the amount of fish to max out all recipes
- `get_recipe(name=None)`: Get the recipe for a specific item

