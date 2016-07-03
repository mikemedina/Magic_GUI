from json import dump, load


path = "./res/history.json"

def update_history(player):
    """Update the player's wins and health"""

    data = {}
    with open(path, 'r') as f:
        data = load(f)

    try:
        data[player.name]['health'] = player.health
        data[player.name]['wins'] = player.wins
    except KeyError:
        data[player.name] = {'health': player.health,
                             'wins': player.wins}

    with open(path, 'w') as f:
        dump(data, f)

def load_stats(player):
    """Look up player stats from the history file"""

    data = {}
    with open(path, 'r') as f:
        data = load(f)

    wins = data[player.name]['wins']
    health = data[player.name]['health']

    return wins, health

