from flask import Flask, request, render_template
from html_template_functions import *

app = Flask(__name__)

@app.route('/')
def my_form():
    a = """
    <h1>Welcome to the Movie Recommendation Engine!</h1>
    <h4>Please enter your movie below:</h4>
    <form method="POST">
        <input name="text">
        <input type="submit">
    </form>
    """
    return a

@app.route('/', methods=['POST'])
def my_form_post():
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
    a = """
    <h1>Welcome to the Movie Recommendation Engine!</h1>
    <h4>Type in your favorite movie's IMBD ID below, to get our top 5 recommendations:</h4>
    """
    return a


# @app.route('/get_movie_rec', methods=['POST'])
# def my_form_post():
#     imbd_id = request.form['text']
#     return str(imbd_id)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)