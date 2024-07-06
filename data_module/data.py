import json
from rich import print as rprint
from datetime import datetime
import os

data = []
maxed_list = set()
ingredients = {}

try:
  with open('json/data.json') as file:
    data = json.load(file)
except FileNotFoundError:
  rprint("[bold red]No data file found. Please run:")
  print("cp data_module/data.json.template json/data.json")

with open('json/maxed_fish.json') as file:
  maxed_list = set(json.load(file))

with open('json/ingredients.json') as file:
  ingredients = json.load(file)

def save_data():
  with open('json/data.json', 'w') as file:
    json.dump(data, file, indent=2)

def create_backup():
  if not os.path.exists('json/backups'):
    os.makedirs('json/backups')
  with open(f"json/backups/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json", 'w') as file:
    json.dump(data, file, indent=2)

  print("Created backup: " + file.name)

def find_backups():
  backups = []
  for file in os.listdir('json/backups'):
    backups.append(file)
  return backups

def restore_backup():
  backups = find_backups()
  print("Which backup would you like to load? q to cancel")

  for index, backup in enumerate(backups):
    print(f"{index + 1}: {backup}")

  while True:
    try:
      inp = input("Enter choice: ").strip()
      if inp == 'q':
        print("Cancelled")
        return

      index = int(inp) - 1
      backup = backups[index]
      break
    except (ValueError, IndexError):
      print("Invalid choice")
      continue

  with open(f"json/backups/{backup}") as file:
    global data
    data = json.load(file)
  save_data()
  print("Backup restored from " + backup)
