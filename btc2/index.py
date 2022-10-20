from flask import render_template
from btc2 import app, dao


@app.route('/')
def home():
    categories = dao.load_json()
    return render_template('index.html', cate = categories)

if __name__ == '__main__':
    app.run(debug = True)

