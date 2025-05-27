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
    try:
        print("Starting Flask server...")
        print(f"Routes: {[str(p) for p in app.url_map.iter_rules()]}")
        print(f"Flask app: {app}")
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Failed to start server: {str(e)}")
        raise