import os
import subprocess
import threading
import openai

from dotenv import load_dotenv

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from flashcard_generator import generate_flashcards

load_dotenv()

# Specify OpenAI API key
openai.api_key = os.environ["API_KEY"]

def clear_default_content(event):
    # Default content when the user starts typing
    current_content = entry.get("1.0", tk.END).strip()
    if current_content == "word1, word2, word3, word4":
        entry.delete("1.0", tk.END)

def button_click():
    input_text = entry.get("1.0", tk.END).strip()  # Retrieve the text from line 1 to the end
    language = language_combobox.get() # Get the desired language
    input_language = input_language_combobox.get() # Get the input language

    if not input_text:
        tk.messagebox.showerror("Error", "No input")
        return

    # Disable the button while generating flashcards
    window.button.config(state=tk.DISABLED)

    # Create a thread for generating flashcards
    thread = threading.Thread(target=generate_flashcards, args=(input_text, language, input_language, window.loading_label, window.button, window.progress_bar))
    thread.start()

def about():
    about_text = "Flashcard Generator\nVersion 0.1.0\nGitHub: https://github.com/lhfdv"
    messagebox.showinfo("About", about_text)

def close():
    window.destroy()

# Main window settings
window = tk.Tk()
window.title("Flashcard Generator")

# Menu
menu = tk.Menu(window)
window.config(menu=menu)

# "About"
about_menu = tk.Menu(menu)
about_menu.add_command(label="About", command=about)
menu.add_cascade(label="Help", menu=about_menu)

# "Close"
menu.add_command(label="Close", command=close)

# Window fixed size
window_width = 555
window_height = 285
window.geometry(f"{window_width}x{window_height}")

# Label for the input
label = tk.Label(window, text="Enter words to generate cards:")
label.grid(row=0, column=0, columnspan=2, pady=10)

# Input field for words
entry = tk.Text(window, height=5)
entry.grid(row=1, column=0, columnspan=2, pady=5)
entry.insert("1.0", "word1, word2, word3, word4")  # Set the default content
entry.bind("<FocusIn>", clear_default_content)

# Label for the language selection
input_language_label = tk.Label(window, text="Select input language:")
input_language_label.grid(row=2, column=0, pady=5)

# Create a Combobox for language selection with default options
input_language_combobox = ttk.Combobox(window, values=["Brazilian Portuguese", "English"])
input_language_combobox.current(0)  # Set the default selection
input_language_combobox.grid(row=3, column=0, pady=5)

# Label for the language selection
language_label = tk.Label(window, text="Select output language:")
language_label.grid(row=2, column=1, pady=5)

# Combobox for language selection with default options
language_combobox = ttk.Combobox(window, values=["Spanish", "French", "Italian"])
language_combobox.current(0)  # Set the default selection
language_combobox.grid(row=3, column=1, pady=5)

# Label for the loading message
loading_label = tk.Label(window, text="")
window.loading_label = loading_label  # Assign loading_label to window.loading_label
loading_label.grid(row=4, columnspan=2)

# Progress bar - Incomplete
progress_bar = ttk.Progressbar(window, mode="determinate")
window.progress_bar = progress_bar  # Assign progress_bar to window.progress_bar
progress_bar.grid(row=5, columnspan=2, pady=5)

# Generate button
window.button = tk.Button(window, text="Generate", command=button_click)
window.button.grid(row=6, columnspan=2, pady=5)

window.mainloop()
