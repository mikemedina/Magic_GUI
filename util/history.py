from json import dump, load
import logging

path = "./res/history.json"

def update_history(player):
    """Update the player's wins and health"""
    history = load_history()

    try:
        history[player.name]['color'] = player.color
        history[player.name]['health'] = player.health
        history[player.name]['wins'] = player.wins
    except KeyError:
        history[player.name] = {'color': player.color, 'health': player.health, 'wins': player.wins}

    with open(path, 'w') as history_file:
        dump(history, history_file)

def load_player(player_name):
    """Look up a player from the history file"""
    history = load_history()

    health = history[player_name]['health']
    wins = history[player_name]['wins']
    color = history[player_name]['color']

    return player_name, color, health, wins

def load_all_players():
    """Return a dictionary of all players from the history file"""
    history = load_history();

    wins = history[player_name]['wins']
    health = history[player_name]['health']

    return wins, health   

def load_history():
    """Load the history file and return it as a dictionary"""
    history = {}
    with open(path, 'r') as history_file:
        history = load(history_file)

    return history

