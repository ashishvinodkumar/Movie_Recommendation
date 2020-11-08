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

    #return return_search_results(your_pick)
    error_code, html = return_search_results(your_pick)
    if error_code == -1:
         html = "<h1>Please try a different movie! <br>Search not found...</h1>"

    html = html + "<br>" + """
    <p align="center"><a href=get_movie_rec ><button class=grey style="height:75px;width:150px">Click here to Proceed</button></a></p>
    """
    return html


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