from flask import Flask, render_template, request, jsonify
import App_Logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-story', methods=['POST'])
def generate_story():
    data = request.get_json()
    user_instructions = data['userInstructions']
    chosen_types = data['availableType']
    story_length = data['storyLength']

    # Call your App_Logic to generate the story
    story_name, story = App_Logic.generateStory(user_instructions, chosen_types, story_length)

    # Return the generated story to the frontend
    return jsonify({
        'storyName': story_name,
        'story': story
    })

if __name__ == '__main__':
    app.run(debug=True)
