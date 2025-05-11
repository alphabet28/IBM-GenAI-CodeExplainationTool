# AI Story Generator

A fun and interactive tool that lets you generate unique stories by selecting a genre and providing a few keywords. The story is generated using Cohere's powerful language model.

## Features

- **Genre Selection**: Choose from multiple genres such as Adventure, Sci-Fi, or Mystery.
- **Customizable Story Elements**: Input character names, settings, and key events for a more personalized story.
- **Story Generation**: Using Cohere's language model, generate a short story based on your selections.
- **Interactive**: Generate new stories by submitting different inputs.

## Technologies Used

- **Python**: For backend development.
- **Flask**: Web framework for building the web app.
- **Cohere API**: For AI-powered story generation.
- **HTML/CSS**: Frontend for user interaction.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/AI-Story-Generator.git
   cd AI-Story-Generator
   ```
# Install the required dependencies:

You can install the required packages by running:

pip install -r requirements.txt

#Set up Cohere API:

Sign up at Cohere to get your API key.

Replace YOUR_COHERE_API_KEY in app.py with your actual API key.

#Run the application:

In the project directory, run:

python app.py

# Access the application:

Open your browser and go to http://127.0.0.1:5000/ to start generating stories.

# How It Works

Select a Genre: Choose the genre of the story from the dropdown menu (e.g., Adventure, Sci-Fi, Mystery).

Enter Story Details: Provide a character name, setting, and key event that you want to be included in the story.

Generate Story: Submit the form, and the app will use Cohere's API to generate a short story based on your inputs.

Get Your Story: The generated story will be displayed, and you can tweak it by submitting new inputs.

# Project Structure

AI-Story-Generator/
├── app.py            # Main Python file for Flask backend
├── templates/
│   └── index.html    # HTML file for frontend UI
└── static/
    └── style.css     # CSS file for styling
