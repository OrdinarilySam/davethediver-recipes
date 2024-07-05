import json
from rich import print
import datetime
import os

data = []
maxed_list = set()
ingredients = {}

try:
  with open('json/data.json') as file:
    data = json.load(file)
except FileNotFoundError:
  print("[bold red]No data file found. Please run:")
  print("cp data_module/data.json.template json/data.json")

with open('json/maxed_fish.json') as file:
  maxed_list = set(json.load(file))

with open('json/ingredients.json') as file:
  ingredients = json.load(file)

def save_data():
  with open('json/data.json', 'w') as file:
    json.dump(data, file, indent=2)

def create_backup():
  with open(f"json/backups/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json", 'w') as file:
    json.dump(data, file, indent=2)

def find_backups():
  backups = []
  for file in os.listdir('json/backups'):
    backups.append(file)
  return backups

def restore_backup(backup):
  with open(f"json/backups/{backup}") as file:
    data = json.load(file)
  save_data()
