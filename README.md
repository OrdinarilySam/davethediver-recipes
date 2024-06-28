# Dave the Diver Recipes
<div>
<img src = "https://github.com/OrdinarilySam/davethediver-recipes/assets/100721569/b5446e95-39b1-46b8-9640-3c1e19f02df9"
  width=300
  height=300>
</div>
<h3> Use this repo to figure out how many fish you need to max out your recipes in Dave the Diver. </h3>

<h4>Requirements: </h4>
<ul>
  <li>Python 3.10+</li>
</ul>
<hr>

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
<hr>

**Available Functions**:
optionally include a name to search for a recipe, leaving blank will return all recipes
- `calculate_amounts(name=None)`: Calculate the amount of fish to max out all recipes
  - name to search for fish
- `calculate_recipe(name=None)`: Calculate the amount of fish to max out a specific recipe
  - name to search for recipe
- `get_recipe(name=None)`: Get the recipe for a specific item
  - name to search for recipe
- `reset()`: Reset the data file to the default values
