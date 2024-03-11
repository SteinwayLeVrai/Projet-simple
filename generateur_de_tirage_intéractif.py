import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

# Grille des gains 
gains = {
    (5, 2): 150000000,
    (5, 1): 200738,
    (5, 0): 20851,
    (4, 2): 1299,
    (4, 1): 120,
    (3, 2): 57,
    (4, 0): 39,
    (2, 2): 14,
    (3, 1): 11.26,
    (3, 0): 9.32,
    (1, 2): 6.75,
    (0, 2): 0,  # Pas de gain pour 0 numéro et 2 étoiles dans la grille donnée
    (2, 1): 5.58,
    (0, 1): 0,  # Pas de gain pour 0 numéro et 1 étoile dans la grille donnée
    (2, 0): 4
}

# Generate random numbers and stars
def generate_random_numbers():
    numbers = []
    while len(numbers) < 5:
        num = random.randint(1, 50)
        if num not in numbers:
            numbers.append(num)
    return sorted(numbers)

def generate_random_stars():
    stars = []
    while len(stars) < 2:
        star = random.randint(1, 12)
        if star not in stars:
            stars.append(star)
    return sorted(stars)

# Fonction pour obtenir le gain
def get_gain(numbers_correct, stars_correct):
    return gains.get((numbers_correct, stars_correct), 0)  # Retourne 0 si la combinaison n'existe pas dans la grille

# Define the application class
class EuroMillionsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Euro Millions - My Million')
        
        self.selected_numbers = []
        self.selected_stars = []
        
        # Define the styles
        style = ttk.Style(self)
        style.configure('TButton', font=('Arial', 12))
        style.configure('TLabel', font=('Arial', 12), padding=10)
        
        # Center the window
        self.geometry('+{}+{}'.format(int(self.winfo_screenwidth()/2 - 300), int(self.winfo_screenheight()/2 - 300)))
        
        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Header
        header = ttk.Label(self, text='Euro Millions - My Million', font=('Arial', 18, 'bold'))
        header.pack()

        # Date label
        date_label = ttk.Label(self, text='Jouer pour 150 Millions €')
        date_label.pack()

        # Numbers frame
        numbers_frame = ttk.Frame(self)
        numbers_frame.pack(pady=10)

        # Number buttons
        for i in range(1, 51):
            btn = ttk.Button(numbers_frame, text=str(i), command=lambda i=i: self.number_selected(i))
            btn.grid(row=(i-1)//5, column=(i-1)%5, padx=5, pady=5)

        # Selected numbers label
        self.selected_numbers_label = ttk.Label(self, text='Numéros sélectionnés: ')
        self.selected_numbers_label.pack()

        # Stars frame
        stars_frame = ttk.Frame(self)
        stars_frame.pack(pady=10)

        # Star buttons
        for i in range(1, 13):
            btn = ttk.Button(stars_frame, text=str(i), command=lambda i=i: self.star_selected(i))
            btn.grid(row=(i-1)//2, column=(i-1)%2, padx=5, pady=5)

        # Selected stars label
        self.selected_stars_label = ttk.Label(self, text='Étoiles sélectionnées: ')
        self.selected_stars_label.pack()

        # Submit button
        submit_btn = ttk.Button(self, text="Jouer !", command=self.check_results)
        submit_btn.pack(pady=20)

    def update_labels(self):
        self.selected_numbers_label.config(text=f'Numéros sélectionnés: {", ".join(map(str, self.selected_numbers))}')
        self.selected_stars_label.config(text=f'Étoiles sélectionnées: {", ".join(map(str, self.selected_stars))}')

    def number_selected(self, number):
        if number not in self.selected_numbers:
            if len(self.selected_numbers) < 5:
                self.selected_numbers.append(number)
                self.selected_numbers.sort()
            else:
                messagebox.showwarning('Attention', 'Vous ne pouvez sélectionner que 5 numéros.')
        else:
            self.selected_numbers.remove(number)
        self.update_labels()

    def star_selected(self, star):
        if star not in self.selected_stars:
            if len(self.selected_stars) < 2:
                self.selected_stars.append(star)
                self.selected_stars.sort()
            else:
                messagebox.showwarning('Attention', 'Vous ne pouvez sélectionner que 2 étoiles.')
        else:
            self.selected_stars.remove(star)
        self.update_labels()

    def check_results(self):
        # Generate new winning numbers and stars for each play
        self.winning_numbers = generate_random_numbers()
        self.winning_stars = generate_random_stars()
        correct_numbers = len(set(self.winning_numbers) & set(self.selected_numbers))
        correct_stars = len(set(self.winning_stars) & set(self.selected_stars))
        gain = get_gain(correct_numbers, correct_stars)
        if correct_numbers == 5 and correct_stars == 2:
            messagebox.showinfo('Félicitations', 'Vous avez gagné le jackpot!')
        else:
            messagebox.showinfo('Résultats', f'Votre gain: {gain}€\nNuméros gagnants: {self.winning_numbers}\nÉtoiles gagnantes: {self.winning_stars}')
        self.update_labels()

# Create and run the application
app = EuroMillionsApp()
app.mainloop()






