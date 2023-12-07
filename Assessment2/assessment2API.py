import requests
import tkinter as tk
from tkinter import messagebox

class SportsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sports App")

        self.search_label = tk.Label(root, text="Enter Player/Event:")
        self.search_label.pack()

        self.search_entry = tk.Entry(root)
        self.search_entry.pack()

        self.search_button = tk.Button(root, text="Search", command=self.search_info)
        self.search_button.pack()

    def search_info(self):
        query = self.search_entry.get()
        if query:
            api_key = "3"

            # Search for players by name
            player_url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={query}"
            player_data = self.api_request(player_url)

            if "players" in player_data:
                player_name = player_data["players"][0]["strPlayer"]
                sport = player_data["players"][0]["strSport"]
                description = player_data["players"][0]["strDescriptionEN"]

                messagebox.showinfo("Player Information", f"Player: {player_name}\nSport: {sport}\nDescription: {description}")
                return

            # Search for events by event name
            event_url = f"https://www.thesportsdb.com/api/v1/json/3/searchevents.php?e={query}"
            event_data = self.api_request(event_url)

            if "events" in event_data:
                event_name = event_data["events"][0]["strEvent"]
                season = event_data["events"][0]["strSeason"]

                messagebox.showinfo("Event Information", f"Event: {event_name}\nSeason: {season}")
                return

            messagebox.showinfo("Information", "No results found.")

        else:
            messagebox.showwarning("Warning", "Please enter a team/player/sport/event.")

    def api_request(self, url):
        try:
            response = requests.get(url)
            data = response.json()
            return data

        except requests.ConnectionError:
            messagebox.showerror("Error", "Failed to connect to TheSportsDB API.")
            return {}

if __name__ == "__main__":
    root = tk.Tk()
    app = SportsApp(root)
    root.geometry("350x250")
    root.mainloop()
