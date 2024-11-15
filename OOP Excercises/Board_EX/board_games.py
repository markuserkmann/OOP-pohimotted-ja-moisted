"""Board games."""
from collections import defaultdict


class Statistics:
    def __init__(self, filename: str):
        self.games_list = []
        self.players = {}
        self.games = {}
        self.load_data(filename)

    def load_data(self, filename: str):
        with open(filename, 'r') as file:
            for line in file:
                game_name, players, result_type, results = line.strip().split(';')
                players = players.split(',')
                
                self.games_list.append({
                    "name": game_name,
                    "players": players,
                    "type": result_type,
                    "results": results
                })

                for player in players:
                    if player not in self.players:
                        self.players[player] = {
                            "games_played": defaultdict(int),
                            "wins": defaultdict(int),
                            "losses": defaultdict(int),
                            "points": defaultdict(list)
                        }
                    self.players[player]["games_played"][game_name] += 1

                if game_name not in self.games:
                    self.games[game_name] = {
                        "times_played": 0,
                        "wins": defaultdict(int),
                        "losses": defaultdict(int),
                        "points": defaultdict(list)
                    }
                self.games[game_name]["times_played"] += 1

                if result_type == "points":
                    scores = list(map(int, results.split(',')))
                    winner = players[scores.index(max(scores))]
                    loser = players[scores.index(min(scores))]
                    
                    for player, score in zip(players, scores):
                        self.players[player]["points"][game_name].append(score)
                        self.games[game_name]["points"][player].append(score)

                elif result_type == "places":
                    places = results.split(',')
                    winner = places[0]
                    loser = places[-1]

                elif result_type == "winner":
                    winner = results
                    loser = None

                if winner:
                    self.players[winner]["wins"][game_name] += 1
                    self.games[game_name]["wins"][winner] += 1
                if loser:
                    self.players[loser]["losses"][game_name] += 1
                    self.games[game_name]["losses"][loser] += 1

    def get(self, path: str):
        parts = path.split('/')

        if path == "/players":
            return sorted(list(self.players.keys()))
        elif path == "/games":
            return sorted(list(self.games.keys()))
        elif path == "/total":
            return len(self.games_list)
        elif path.startswith("/total/"):
            result_type = parts[-1]
            return len([game for game in self.games_list if game["type"] == result_type])

        elif parts[1] == "player":
            player_name = parts[2]
            if player_name not in self.players:
                return "Player not found"

            if parts[3] == "amount":
                return sum(self.players[player_name]["games_played"].values())
            elif parts[3] == "favourite":
                games = self.players[player_name]["games_played"]
                if not games:
                    return None
                return max(games.items(), key=lambda x: x[1])[0]
            elif parts[3] == "won":
                return sum(self.players[player_name]["wins"].values())

        elif parts[1] == "game":
            game_name = parts[2]
            if game_name not in self.games:
                return "Game not found"

            if parts[3] == "amount":
                return self.games[game_name]["times_played"]
            elif parts[3] == "player-amount":
                player_counts = [len(game["players"]) for game in self.games_list 
                               if game["name"] == game_name]
                return max(player_counts)
            elif parts[3] == "most-wins":
                wins = self.games[game_name]["wins"]
                if not wins:
                    return None
                return max(wins.items(), key=lambda x: x[1])[0]
            elif parts[3] == "most-frequent-winner":
                wins = self.games[game_name]["wins"]
                if not wins:
                    return None
                win_rates = {}
                for player in wins.keys():
                    games_played = self.players[player]["games_played"][game_name]
                    win_rates[player] = wins[player] / games_played
                return max(win_rates.items(), key=lambda x: x[1])[0]
            elif parts[3] == "most-losses":
                losses = self.games[game_name]["losses"]
                if not losses:
                    return None
                return max(losses.items(), key=lambda x: x[1])[0]
            elif parts[3] == "most-frequent-loser":
                losses = self.games[game_name]["losses"]
                if not losses:
                    return None
                loss_rates = {}
                for player in losses.keys():
                    games_played = self.players[player]["games_played"][game_name]
                    loss_rates[player] = losses[player] / games_played
                return max(loss_rates.items(), key=lambda x: x[1])[0]
            elif parts[3] == "record-holder":
                points = self.games[game_name]["points"]
                if not points:
                    return None
                max_points = {player: max(scores) for player, scores in points.items()}
                return max(max_points.items(), key=lambda x: x[1])[0]

        return "Unknown path"

if __name__ == "__main__":
    stats = Statistics("data.txt")
    
    print("All players:", stats.get("/players"))
    print("All games:", stats.get("/games"))
    print("Total games:", stats.get("/total"))
    print("Total points games:", stats.get("/total/points"))
    
    print("Player games:", stats.get("/player/joosep/amount"))
    print("Player favorite game:", stats.get("/player/joosep/favourite"))
    
    print("Game amount:", stats.get("/game/7 wonders/amount"))
    print("Game max players:", stats.get("/game/7 wonders/player-amount"))
    print("Game most wins:", stats.get("/game/7 wonders/most-wins"))