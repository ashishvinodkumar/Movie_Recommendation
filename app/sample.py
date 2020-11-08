from flask import Flask
from flask import jsonify
app = Flask(__name__)

# Welcome + Search
@app.route('/')
def welcome_and_search():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World!!! cd'

# Select Movie
@app.route('/echo/<imbd>')
def select_movie(movie):
    print(f"This was placed in the url: new-{movie}")
    val = {"new-name": movie}
    return jsonify(val)

# Get Movie Recommendation
@app.route('/echo/<name>')
def get_recommendation(imdb):
    print(f"This was placed in the url: new-{imdb}")
    val = {"new-name": imdb}
    return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)