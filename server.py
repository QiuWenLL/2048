from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route('/scores')
def get_scores():
    # 读取分数文件
    if os.path.exists('scores.json'):
        with open('scores.json', 'r', encoding='utf-8') as f:
            try:
                scores = json.load(f)
            except json.JSONDecodeError:
                scores = []
    else:
        scores = []
    
    return jsonify(scores)

@app.route('/')
def show_scores():
    return render_template('scores.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)