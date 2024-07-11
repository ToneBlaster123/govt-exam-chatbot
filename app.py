from flask import Flask, request, jsonify
from flask_cors import CORS
from actions import ActionGetExamInfo

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    action = ActionGetExamInfo()
    response = action.get_exam_info(user_message)
    return jsonify(response)Q
