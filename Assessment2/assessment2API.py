import requests
import tkinter as tk
from tkinter import ttk
from urllib.parse import quote

class SportsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sports Information App")

        self.style = ttk.Style()
        self.style.configure("TFrame", background="#111")
        self.style.configure("TLabel", background="#111", foreground="#00a8cc", font=('Helvetica', 12))
        self.style.configure("TButton", background="#00a8cc", foreground="black", font=('Helvetica', 12))

        self.frame = ttk.Frame(master)
        self.frame.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.label_team_name = ttk.Label(self.frame, text="Enter Team Name:")
        self.label_team_name.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.entry_team_name = ttk.Entry(self.frame, width=30)
        self.entry_team_name.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        self.button_get_team_info = ttk.Button(self.frame, text="Get Team Info", command=self.get_team_info)
        self.button_get_team_info.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        self.button_get_players = ttk.Button(self.frame, text="Get Players", command=self.get_team_players)
        self.button_get_players.grid(row=0, column=3, pady=10, padx=10, sticky="w")

        self.button_list_countries = ttk.Button(self.frame, text="List All Countries", command=self.list_all_countries)
        self.button_list_countries.grid(row=1, column=0, pady=10, padx=10, sticky="w", columnspan=4)

        self.button_list_sports = ttk.Button(self.frame, text="List All Sports", command=self.list_all_sports)
        self.button_list_sports.grid(row=2, column=0, pady=10, padx=10, sticky="w", columnspan=4)

        self.button_list_loved_teams_players = ttk.Button(self.frame, text="List Loved Teams and Players", command=self.list_loved_teams_players)
        self.button_list_loved_teams_players.grid(row=3, column=0, pady=10, padx=10, sticky="w", columnspan=4)

        self.result_frame = ttk.Frame(master)
        self.result_frame.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        self.result_label = ttk.Label(self.result_frame, text="", wraplength=500, justify="left", anchor="w")
        self.result_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

    def get_team_info(self):
        team_name = self.entry_team_name.get()
        team_name_encoded = quote(team_name)

        if team_name:
            api_url = f"https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t={team_name_encoded}"

            try:
                team_data = self.get_data_from_api(api_url)
                if "teams" in team_data and team_data["teams"]:
                    self.display_team_info(team_data["teams"][0])
                else:
                    self.result_label.config(text="Team not found.")
            except requests.RequestException as e:
                self.result_label.config(text=f"Error: {str(e)}")
        else:
            self.result_label.config(text="Please enter a team name.")

    def get_team_players(self):
        team_name = self.entry_team_name.get()
        team_name_encoded = quote(team_name)

        if team_name:
            api_url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?t={team_name_encoded}"

            try:
                players_data = self.get_data_from_api(api_url)
                if "player" in players_data and players_data["player"]:
                    self.display_team_players(players_data["player"])
                else:
                    self.result_label.config(text="No players found for the team.")
            except requests.RequestException as e:
                self.result_label.config(text=f"Error: {str(e)}")
        else:
            self.result_label.config(text="Please enter a team name.")

    def list_all_countries(self):
        api_url = "https://www.thesportsdb.com/api/v1/json/3/all_countries.php"

        try:
            countries_data = self.get_data_from_api(api_url)
            print(f"Countries API Response: {countries_data}")  # Print API response for debugging

            if "countries" in countries_data and countries_data["countries"]:
                self.display_countries(countries_data["countries"])
            else:
                self.result_label.config(text="No countries found.")
        except requests.RequestException as e:
            self.result_label.config(text=f"Error: {str(e)}")

    def list_all_sports(self):
        api_url = "https://www.thesportsdb.com/api/v1/json/3/all_sports.php"

        try:
            sports_data = self.get_data_from_api(api_url)
            print(f"Sports API Response: {sports_data}")  # Print API response for debugging

            if "sports" in sports_data and sports_data["sports"]:
                self.display_sports(sports_data["sports"])
            else:
                self.result_label.config(text="No sports found.")
        except requests.RequestException as e:
            self.result_label.config(text=f"Error: {str(e)}")

    def list_loved_teams_players(self):
        username = "debsicat22"  # Replace with the actual username
        api_url = f"https://www.thesportsdb.com/api/v1/json/3/searchloves.php?u={username}"

        try:
            loved_data = self.get_data_from_api(api_url)
            print(f"Loved Teams and Players API Response: {loved_data}")  # Print API response for debugging

            if "loved" in loved_data and loved_data["loved"]:
                self.display_loved_teams_players(loved_data["loved"])
            else:
                self.result_label.config(text="No loved teams and players found for the user.")
        except requests.RequestException as e:
            self.result_label.config(text=f"Error: {str(e)}")

    def get_data_from_api(self, api_url):
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data

    def display_team_info(self, team_info):
        info_text = f"Team Name: {team_info['strTeam']}\n"
        info_text += f"Sport: {team_info['strSport']}\n"
        info_text += f"Stadium: {team_info['strStadium']}\n"
        info_text += f"Description: {team_info['strDescriptionEN']}"
        self.result_label.config(text=info_text)

    def display_team_players(self, players):
        players_text = "Players:\n"
        for player in players:
            players_text += f"{player['strPlayer']}\n"
        self.result_label.config(text=players_text)

    def display_countries(self, countries):
        if isinstance(countries, list):
            countries_text = "All Countries:\n"
            for country in countries:
                if isinstance(country, (str, int)):
                    countries_text += f"{country}\n"
                elif isinstance(country, dict) and 'name_en' in country:
                    countries_text += f"{country['name_en']}\n"
                else:
                    countries_text += "N/A\n"
            self.result_label.config(text=countries_text)
        else:
            self.result_label.config(text="No countries found.")

    def display_sports(self, sports):
        if isinstance(sports, list):
            sports_text = "All Sports:\n"
            for sport in sports:
                if isinstance(sport, (str, int)):
                    sports_text += f"{sport}\n"
                elif isinstance(sport, dict) and 'strSport' in sport:
                    sports_text += f"Sport: {sport['strSport']}\n"
                    if 'strSportDescription' in sport:
                        sports_text += f"Description: {sport['strSportDescription']}\n"
                    sports_text += "\n"
                else:
                    sports_text += "N/A\n"
            self.result_label.config(text=sports_text)
        else:
            self.result_label.config(text="No sports found.")

    def display_loved_teams_players(self, loved_data):
        loved_text = "Loved Teams and Players:\n"
        for entry in loved_data:
            if 'strTeam' in entry:
                loved_text += f"Team: {entry['strTeam']}\n"
            if 'strPlayer' in entry:
                loved_text += f"Player: {entry['strPlayer']}\n"
            loved_text += "\n"
        self.result_label.config(text=loved_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = SportsApp(root)
    root.mainloop()
