<h1 align="center">Dave the Diver Recipes</h1>
<div align="center">
<img src = "https://github.com/OrdinarilySam/davethediver-recipes/assets/100721569/b5446e95-39b1-46b8-9640-3c1e19f02df9"
  width=150
  height=150>
</div>
<h3 align="center">An all in one CLI tool to figure out how many fish you need to max out your recipes in Dave the Diver.</h3>
<hr>
<h4>Requirements: </h4>
<ul>
  <li>Python 3.10+</li>
  <li>Rich</li>
  <li>Dave the Diver</li>
</ul>

**Installation and Setup**:
1. Clone the repo
```sh
git clone https://github.com/OrdinarilySam/davethediver-recipes.git
cd davethediver-recipes
```

2. Create your own data file
```sh
cp data_module/data.json.template json/data.json
```

3. Create a venv and install requirements
```sh
python3 -m venv <name>
source <name>/bin/activate
pip install -r requirements.txt
```
<hr>

**Usage**:
Alright, you've got it set up, now what?

There are two paths to go down here, but the CLI tool is just better.

1. **CLI Tool**:
```sh
python cli.py
```

You're going to be presented with options, and you can choose what you want from there. 
Everything in the CLI is pretty self-explanatory.

2. **Interactive Shell**:
```sh
python -i interactive.py
```

This is a bit more freeform. You can call functions directly and create your own local variables to play with.
The problem is there's no help or guidance, so you'll have to know what functions you're calling.

Here are the options. When a name isn't available, you will be prompted.

<hr>

**Available Functions**:
optionally include a name to search for, leaving blank will return all
```python
calculate_amounts(filters={})
```
1. Use this function to calculate the amount of fish needed to max out recipes.
  - this takes in a dictionary of filters
  - when left blank, this will display all ingredients
  - filters can have keys for 'ingredient', 'category', 'num_ingredients' 
    - ingredient: takes in a list of ingredients to filter by
    - category: takes in a string of the category. Options: 'seafood', 'plants', 'seasoning'
    - num_ingredients: takes in an integer to filter by the number of distinct ingredients in the recipe

```python
calculate_recipe()
```
2. Use this function to search for a specific recipe and calculate the amount of fish need to max just that recipe.

```python
get_recipe()
```
3. Use this function to search for a specific recipe and print it.

```python
get_recipe_from_ingredient()
```
4. Use this function to search for a specific ingredient and print all recipes that use it. 

```python
upgrade_recipe()
``` 
5. Use this function to upgrade a single recipe. (Also set specific level)

```python
continuous_upgrade()
```
6. Use this function to continuously upgrade recipes. Use Ctrl-D or Ctrl-C to stop.

```python
reset()
```
7. Use this function to reset the data file to the default values.


**Utility Functions**:
```python
fuzzy_find_ingredients(search=str)
fuzzy_find_recipes(search=str)
create_backup()
restore_backup()
save_data() # use this if modifying the data list directly
``` 
