from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        personaje_id = request.form['personaje_id']
        url = f'https://spapi.dev/api/characters/{personaje_id}'
        response = requests.get(url)
        data = response.json()
        return render_template('index.html', data=data)
    return render_template('index.html')

@app.route('/apis')
def apis():
    return render_template('apis.html')

if __name__ == '__main__':
    app.run(debug=True)
