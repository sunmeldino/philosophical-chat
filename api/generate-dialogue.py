from flask import Flask, request, jsonify 
import random 
 
app = Flask(__name__) 
 
nicknames = ['Philosopher1', 'Philosopher2', 'Thinker1', 'Thinker2'] 
 
"# Dummy data for dialogue generation" 
dialogues = [ 
"    'What is the essence of our homeland?', " 
"    'Our homeland lives in our hearts, not on any map.', " 
"    'Love for our land transcends borders.', " 
"    'It's a spiritual connection, not a physical one.'" 
] 
 
"@app.route('/generate-dialogue', methods=['POST'])" 
"def generate_dialogue():" 
"    data = request.json" 
"    nickname = random.choice(data['nicknames'])" 
"    message = random.choice(dialogues)" 
"    has_next = random.choice([True, False])  # Simulate end of conversation" 
"    return jsonify(nickname=nickname, message=message, hasNext=has_next)" 
 
"if __name__ == '__main__':" 
"    app.run(debug=True)" 
