from flask import Flask, render_template, url_for
import anime


app = Flask(__name__, static_url_path='/templates', static_folder='templates')


@app.route('/')
def index():
    mask = anime.animes['score'].isna()
    print(anime.animes.info())
    seasons = anime.get_seasoned_animes(num_of_animes=20, target_season=2015)
    return render_template('index.html', seasons=seasons)


@app.route('/anime/<uid>')
def view_anime(uid):
    target_anime = anime.get_anime(int(uid))
    seasons = anime.get_seasoned_animes(num_of_animes=20, target_season=2020)
    return render_template('anime_page.html', anime=target_anime, seasons=seasons)


@app.route('/<genre>')
def test(genre):
    target_animes = anime.get_animes_by_category(genre)
    return render_template('genre.html', animes=target_animes)




if __name__ == '__main__':
    app.run(debug=True)