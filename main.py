import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database connection
DB_FILE = "voight_kampff.db"

def connect_db():
    return sqlite3.connect(DB_FILE)

# Splash screen
def splash_screen():
    root = tk.Tk()
    root.configure(bg="black")
    root.attributes("-fullscreen", True)
    label = tk.Label(root, text="Voight-Kampff Machine", fg="green", bg="black", font=("Courier New", 24))
    label.pack(pady=50)
    root.after(3000, root.destroy)  # Close after 3 seconds
    root.mainloop()

# Main menu
def main_menu():
    root = tk.Tk()
    root.configure(bg="black")
    root.attributes("-fullscreen", True)
    label = tk.Label(root, text="Main Menu", fg="green", bg="black", font=("Courier New", 24))
    label.pack(pady=20)

    buttons = [
        ("Start Interrogation", lambda: messagebox.showinfo("Info", "Interrogation started")),
        ("Client Management", lambda: messagebox.showinfo("Info", "Client Management")),
        ("Agent Management", lambda: messagebox.showinfo("Info", "Agent Management")),
        ("Empathy Questions", lambda: messagebox.showinfo("Info", "Empathy Questions")),
        ("Maintenance", lambda: messagebox.showinfo("Info", "Maintenance")),
        ("Exit", root.destroy)
    ]

    for text, command in buttons:
        button = tk.Button(root, text=text, fg="green", bg="black", font=("Courier New", 18), command=command)
        button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    splash_screen()
    main_menu()
