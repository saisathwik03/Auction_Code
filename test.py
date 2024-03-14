import random

def read_player_data(filename):
  """
  Reads player data from a CSV file and returns a list of lists.

  Args:
      filename (str): The name of the CSV file containing player data.

  Returns:
      list: A list of lists, where each inner list represents a player's information.

  Raises:
      FileNotFoundError: If the specified file is not found.
  """
  try:
    with open(filename, 'r') as file:
      lines = file.readlines()
  except FileNotFoundError:
    raise FileNotFoundError(f"Error: File '{filename}' not found.")

  data = []
  # Skip the header row
  for line in lines[1:]:
    # Split the line by commas and remove leading/trailing spaces
    fields = [field.strip() for field in line.split(",")]
    data.append(fields)

  return data

def print_random_players(players, num_players):
  """
  Prints details of a specified number of randomly selected players.

  Args:
      players (list): A list of lists, where each inner list represents a player's information.
      num_players (int): The number of players to randomly select and print.
  """
  if num_players > len(players):
    print(f"Error: Requested number of players ({num_players}) exceeds total players ({len(players)}).")
    return

  # Randomly select players without replacement
  selected_players = random.sample(players, num_players)
  for player in selected_players:
    print(player)

# Specify the filename containing player data (replace with your actual filename)
filename = "listofplayer.csv"

# Specify the number of players to randomly select
num_players = 1  # Adjust as needed

try:
  # Read player data from the file
  players = read_player_data(filename)

  # Print details of randomly selected players
  print_random_players(players, num_players)
except FileNotFoundError as e:
  print(e)
