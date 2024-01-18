from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/stock-project')
def stock():
    return render_template('stock.html')


@app.route('/car-project')
def car():
    return render_template('car.html')


@app.route('/movie-project')
def movie():
    return render_template('movie.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
