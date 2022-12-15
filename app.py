from flask import Flask
from dao.movie import MovieDAO
app = Flask(__name__)

movies = MovieDAO()

@app.route('/movie/<title>')
def get_json_by_title(title):  # put application's code here
    return movies.get_by_title(title)

@app.route('/movie/year-to-year/<start>/<end>')
def get_json_for_period(start, end):  # put application's code here
    return movies.get_by_year_period(start, end)

@app.route('/movie/rating/<rating>')
def get_json_by_rating(rating):  # put application's code here
    return movies.get_by_rating(rating)

@app.route('/movie/genre/<genre>')
def get_json_by_genre(genre):  # put application's code here
    return movies.get_by_genre(genre)

if __name__ == '__main__':
    app.run()
