from flask import Flask, request, render_template, redirect, url_for
from html_template_functions import *

app = Flask(__name__)

@app.route('/')
def my_form():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/home', methods=['POST'])
def home_post():
    your_pick = request.form['text']
    error_code, imdbid_list, movie_list = return_search_results(your_pick)
    return render_template('home-post.html', error_code=error_code, imdbid_list=imdbid_list, movie_list=movie_list)


@app.route('/get_movie_rec')
def get_movie_rec():
    return render_template('get_movie_rec.html')


@app.route('/get_movie_rec', methods=['POST'])
def get_movie_rec_post():
    imbd_id = request.form['imbd']
    imdb_list, title_list = get_recommendations(imbd_id)
    return render_template('get_movie_rec-post.html', imdb_list = imdb_list, title_list=title_list)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)