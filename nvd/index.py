from flask import Flask, render_template
import dao

app = Flask(__name__)
@app.route('/')

def index():
    categories = dao.load()
    return render_template('index.html',categories=categories)

if __name__ == '__main__':
    app.run()


