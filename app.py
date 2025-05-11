from flask import Flask, render_template, request
import cohere

app = Flask(__name__)

# Initialize Cohere API client with your API key
cohere_client = cohere.Client("DZJ7lBAZanbfVjbYS1kcdm6alEizoO1gw6Yt6SgU")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        genre = request.form['genre']
        keywords = {
            'character_name': request.form['character_name'],
            'setting': request.form['setting'],
            'key_event': request.form['key_event']
        }

        # Call Cohere API to generate a story based on user input
        story = generate_story(genre, keywords)
        
        return render_template('index.html', story=story)

    return render_template('index.html', story=None)

def generate_story(genre, keywords):
    prompt = f"Write a {genre} story with a character named {keywords['character_name']}, " \
             f"set in {keywords['setting']}, and the key event is {keywords['key_event']}."
    
    response = cohere_client.generate(
        model='xlarge',  # Choose appropriate model size
        prompt=prompt,
        max_tokens=300
    )
    return response.generations[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
