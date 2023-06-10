# Flashcard Generator

This is a Python application that utilizes the AI models to automatically generate flashcards from input words or phrases. This documentation provides an overview of the project structure and guides you through the process of running and modifying the code.

## Project Structure

The Flashcard Generator project consists of the following files:

- `main.py`: The main script.
- `gui.py`: The script that creates the graphical user interface (GUI) and handles user interactions.
- `flashcard_generator.py`: A module containing functions to generate flashcards.

## Getting Started

To run the Flashcard Generator on your local machine, follow these steps:

1. Clone the project repository from GitHub: [https://github.com/lhfdv/flashcard-generator](https://github.com/lhfdv/flashcard-generator)
2. Install the required dependencies by running the following command in the project directory:

   pip install -r requirements.txt

3. Set up the OpenAI API key by creating a .env file in the project directory and adding the following line:

    Copy code
    API_KEY=<your_openai_api_key>
    Replace <your_openai_api_key> with your actual OpenAI API key.

4. Run the main.py script using the following command:

    python main.py

5. The Flashcard Generator GUI will open, allowing you to enter words or phrases and generate flashcards.

## Modifying the Code

The Flashcard Generator code can be modified to customize its behavior and appearance. Here are some common modifications you may want to make:

- **Adding or Removing Output Languages**: Open the `gui.py` file and locate the `language_combobox` variable definition. Modify the `values` attribute of the `Combobox` widget to include or remove the desired output languages.

- **Modifying Input Language Options**: Open the `gui.py` file and locate the `input_language_combobox` variable definition. Modify the `values` attribute of the `Combobox` widget to include or remove the desired input languages.

- **Changing Default Content of the Input Field**: Open the `gui.py` file and locate the `default_content` variable definition. Modify the value assigned to the `default_content` variable to change the default text displayed in the input field.

- **Altering the AI Model Configuration**: Open the `flashcard_generator.py` file and locate the `generate_flashcards` function. Adjust the parameters of the `openai.ChatCompletion.create()` method to modify the AI model configuration.

- **Customizing GUI Elements**: Open the `gui.py` file and locate the relevant GUI element (e.g., labels, buttons, input fields) that you want to customize. Modify the attributes of the GUI element to change its appearance or behavior.

- **Adding or Modifying Functionality**: Identify the relevant functions or code blocks related to the functionality you want to add or modify. Make the necessary changes to implement the desired functionality.

Remember to save your changes after modifying the code and test the program to verify the desired outcomes.

## Additional Information

For more information and support, you can refer to the following resources:

- GitHub Repository: [https://github.com/lhfdv/Anki_Flashcards_GPT](https://github.com/lhfdv/Anki_Flashcards_GPT)
- OpenAI Documentation: [https://docs.openai.com/](https://docs.openai.com/)
- Python Documentation: [https://docs.python.org/](https://docs.python.org/)

## License

GNU General Public License v2.0