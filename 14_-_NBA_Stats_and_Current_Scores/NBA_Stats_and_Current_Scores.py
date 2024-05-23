from requests import get
from pprint import PrettyPrinter

class NBAStats:
    BASE_URL = "https://data.nba.net"
    ALL_JSON = "/prod/v1/today.json"

    def __init__(self):
        self.printer = PrettyPrinter()
        self.links = self.get_links()

    def get_links(self):
        """
        Fetches and returns all links from NBA API.
        """
        data = get(self.BASE_URL + self.ALL_JSON).json()
        return data['links']

    def get_scoreboard(self):
        """
        Fetches and prints current NBA games scoreboard.
        """
        scoreboard = self.links['currentScoreboard']
        games = get(self.BASE_URL + scoreboard).json()['games']

        for game in games:
            home_team = game['hTeam']
            away_team = game['vTeam']
            clock = game['clock']
            period = game['period']

            print("------------------------------------------")
            print(f"{home_team['triCode']} vs {away_team['triCode']}")
            print(f"{home_team['score']} - {away_team['score']}")
            print(f"{clock} - {period['current']}")

    def get_stats(self):
        """
        Fetches and prints NBA team statistics leaders.
        """
        stats = self.links['leagueTeamStatsLeaders']
        teams = get(self.BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

        teams = list(filter(lambda x: x['name'] != "Team", teams))
        teams.sort(key=lambda x: int(x['ppg']['rank']))

        for i, team in enumerate(teams):
            name = team['name']
            nickname = team['nickname']
            ppg = team['ppg']['avg']
            print(f"{i + 1}. {name} - {nickname} - {ppg}")

# Example usage:
if __name__ == "__main__":
    nba_stats = NBAStats()
    nba_stats.get_stats()
