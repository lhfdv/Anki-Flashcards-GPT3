import os
import subprocess
import threading

from dotenv import load_dotenv
import clipboard
import openai

import tkinter as tk
from tkinter import ttk

load_dotenv()

openai.api_key = os.environ["API_KEY"]

def generate_flashcards(input_text):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Create anki flashcards for the following Spanish words, only one output per word.: {input_text}. The output format must be: word in spanish;phrase in spanish;word in english;translated phrase. Example: hola;hola, que tal;hello;hello how are you doing"}
    ]

        # Update the loading label
    loading_label.config(text="Generating flashcards...")

    # Start the progress bar animation
    progress_bar.start()
    window.update()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=2000
    )

    generated_flashcards = response["choices"][0]["message"]["content"]
    with open("flashcards.txt", "w", encoding="utf-8") as f:
        f.write(generated_flashcards)

    # Stop the progress bar animation
    progress_bar.stop()

    # Update the loading label
    loading_label.config(text="Flashcards generated! Saved to 'flashcards.txt'")
    window.update()

    # Open the flashcards.txt file
    subprocess.Popen(["notepad.exe", "flashcards.txt"])

    # Re-enable the button
    button.config(state=tk.NORMAL)

def button_click():
    input_text = entry.get()

    # Disable the button while generating flashcards
    button.config(state=tk.DISABLED)

    # Create a thread for generating flashcards
    thread = threading.Thread(target=generate_flashcards, args=(input_text,))
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
button = tk.Button(window, text="Generate Flashcards", command=button_click)
button.pack()

# Create a label for the loading message
loading_label = tk.Label(window, text="")
loading_label.pack()

# Create a progress bar
progress_bar = ttk.Progressbar(window, mode="indeterminate")
progress_bar.pack(pady=10)

# Start the main event loop
window.mainloop()