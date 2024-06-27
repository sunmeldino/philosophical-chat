from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Configure the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/generate-dialogue', methods=['POST'])
def generate_dialogue():
    data = request.json
    nicknames = data.get('nicknames', ['Philosopher1', 'Philosopher2'])
    context = data.get('context', 'philosophical discussion about love for an abstract homeland')

    conversation = f"{nicknames[0]}: What is the essence of our homeland?\n{nicknames[1]}: Our homeland lives in our hearts, not on any map."

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=conversation,
        max_tokens=150
    )

    message = response.choices[0].text.strip()
    return jsonify(nickname=nicknames[1], message=message, hasNext=True)

if __name__ == '__main__':
    app.run(debug=True)
