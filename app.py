from flask import Flask, request, jsonify
from ai_model import generate_response

app = Flask(__name__)

@app.route('/api/message', methods=['POST'])
def message():
    user_input = request.json.get('message')
    response = generate_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
