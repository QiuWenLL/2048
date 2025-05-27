from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/scores')
def show_scores():
    try:
        with open('scores.json', 'r') as f:
            scores_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        scores_data = {"scores": []}
    
    return render_template('scores.html', scores=scores_data["scores"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)