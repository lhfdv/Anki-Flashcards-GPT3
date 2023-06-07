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

def button_click():
    input_text = entry.get("1.0", tk.END).strip()  # Retrieve the text from line 1 to the end
    language = language_combobox.get() # Get the desired language

    if not input_text:
        tk.messagebox.showerror("Error", "No input")
        return

    # Disable the button while generating flashcards
    window.button.config(state=tk.DISABLED)

    # Create a thread for generating flashcards
    thread = threading.Thread(target=generate_flashcards, args=(input_text, language, window.loading_label, window.button, window.progress_bar))
    thread.start()

# Create the main window
window = tk.Tk()
window.title("Flashcard Generator")

# Set a fixed size for the window
window_width = 580
window_height = 320
window.geometry(f"{window_width}x{window_height}")

# Create a label
label = tk.Label(window, text="Enter words to generate cards:")
label.pack(pady=2)
label = tk.Label(window, text="Example: word1, word2, word3, word4")
label.pack(pady=2)

# Create an input field for words
entry = tk.Text(window, height=5)
entry.pack(pady=5)

# Create a label for the language selection
language_label = tk.Label(window, text="Select language:")
language_label.pack(pady=10)

# Create a Combobox for language selection with default options
language_combobox = ttk.Combobox(window, values=["Spanish", "French", "Italian", "Japanese"])
language_combobox.current(0)  # Set the default selection
language_combobox.pack(pady=5)

# Create a label for the loading message
loading_label = tk.Label(window, text="")
window.loading_label = loading_label  # Assign loading_label to window.loading_label
loading_label.pack()

# Create a progress bar
progress_bar = ttk.Progressbar(window, mode="determinate")
window.progress_bar = progress_bar  # Assign progress_bar to window.progress_bar
progress_bar.pack(pady=10)

# Create a button
window.button = tk.Button(window, text="Generate", command=button_click)
window.button.pack(pady=10)

# Start the main event loop
window.mainloop()