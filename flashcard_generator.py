import os
import openai
import subprocess
import time
from tkinter import messagebox

# Specify the output folder path
output_folder = "output"

def generate_flashcards(input_text, language, input_language, loading_label, button, progress_bar):
    # GPT Prompt
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Create anki flashcards for the following {language} words in {input_language}, only one output per word is allowed.: {input_text}. The output format must be: word in spanish;phrase in spanish;word in english;translated phrase. Example: hola;hola, que tal;hello;hello how are you doing"}
    ]

    # Update the loading label
    loading_label.config(text="Generating flashcards...")

    # GPT settings
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=2000
    )

    generated_flashcards = response["choices"][0]["message"]["content"]

    timestamp = time.strftime("%Y%m%d%H%M%S")
    file_name = f"flashcards_{timestamp}.txt"

    # Specify the file path in the output folder
    file_path = os.path.join(output_folder, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(generated_flashcards)

    # Update the loading label
    loading_label.config(text="Saved to 'output/${file_name}'")

    # Open the flashcards.txt file
    subprocess.Popen(["notepad.exe", file_path])

    # Re-enable the button
    button.config(state="normal")

    # Update the progress bar to 100%
    progress_bar["value"] = 100

