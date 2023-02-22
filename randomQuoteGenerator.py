import tkinter as tk
import requests
import random

class QuoteGenerator:
    def __init__(self, genres):
        self.genres = genres
        self.genre = None
        self.quote = None
        self.author = None
    
    def get_quote(self):
        # randomly select a genre from the list of desired genres
        self.genre = random.choice(self.genres)

        # make an HTTP request to the API with the selected genre and print the random quote
        url = f'https://quote-garden.onrender.com/api/v3/quotes/random?genre={self.genre}'
        response = requests.get(url)

        # check if the request was successful
        if response.status_code == 200:
            # extract the quote from the API response body 
            quote_data = response.json()['data'][0]
            self.quote = quote_data['quoteText']
            self.author = quote_data['quoteAuthor']
        else:
            print(f'Error getting quote for genre {self.genre}: {response.status_code}')

class QuoteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quote App")
        self.generator = QuoteGenerator(['strength', 'success', 'sympathy', 'technology', 'positive', 'power'])

        # create the UI
        self.label = tk.Label(master, text="", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.button = tk.Button(master, text="Generate Quote", font=("Helvetica", 12), command=self.get_new_quote)
        self.button.pack(anchor="sw", padx=5, pady=10)
        self.button.place(x=20, y=300)

        self.quote_label = tk.Label(master, text='', font=("Helvetica", 12, "italic"), justify="center", wraplength=280)
        self.quote_label.pack(pady=10)

        self.copy_button = tk.Button(master, text="Copy Quote", font=("Helvetica", 12), command=self.copy_quote)
        self.copy_button.pack(anchor="center", padx=5, pady=10)
        self.copy_button.place(x=185, y=300)

        self.return_button = tk.Button(master, text="Return", font=("Helvetica", 12), command=self.return_to_main)
        self.return_button.pack(side=tk.RIGHT, padx=5, pady=10)
        self.return_button.place(x=320, y=300)

    def get_new_quote(self):
        self.generator.get_quote()
        self.display_quote()

    def display_quote(self):
        self.quote_label.config(text=f'"{self.generator.quote}"\n- {self.generator.author}')

    def copy_quote(self):
        self.master.clipboard_append(f'"{self.generator.quote}"')
        self.master.clipboard_append(f"\n- {self.generator.author}")

    def return_to_main(self):
        self.label.config(text="")
        self.quote_label.config(text='') 

root = tk.Tk()
root.geometry('400x350')  
app = QuoteApp(root)
root.mainloop()
