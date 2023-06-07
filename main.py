import os
import subprocess
import threading
import openai
from dotenv import load_dotenv
import tkinter as tk
from tkinter import ttk
from flashcard_generator import generate_flashcards

load_dotenv()

# Specify OpenAI API key
openai.api_key = os.environ["API_KEY"]

def button_click():
    input_text = entry.get()

    # Disable the button while generating flashcards
    window.button.config(state=tk.DISABLED)

    # Create a thread for generating flashcards
    thread = threading.Thread(target=generate_flashcards, args=(input_text, window.loading_label, window.button))
    thread.start()

# Create the main window
window = tk.Tk()
window.title("Flashcard Generator")

# Set a fixed size for the window
window_width = 400
window_height = 300
window.geometry(f"{window_width}x{window_height}")

# Create a label
label = tk.Label(window, text="Enter words to generate flashcards")
label.pack()

# Create an input field
entry = tk.Entry(window)
entry.pack()

# Create a button
window.button = tk.Button(window, text="Generate Flashcards", command=button_click)
window.button.pack()

# Create a label for the loading message
loading_label = tk.Label(window, text="")
window.loading_label = loading_label  # Assign loading_label to window.loading_label
loading_label.pack()

# Create a progress bar
progress_bar = ttk.Progressbar(window, mode="indeterminate")
window.progress_bar = progress_bar  # Assign progress_bar to window.progress_bar
progress_bar.pack(pady=10)

# Start the main event loop
window.mainloop()
