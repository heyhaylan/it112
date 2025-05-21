from flask import Flask, render_template, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///films.sqlite3'
db = SQLAlchemy(app)


# database
class Film(db.Model):
    id = db.Column('film_id', db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.String(5), nullable=False)

    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    @property
    def serialize(self):
         return {
              'id': self.id,
              'title': self.title,
              'genre': self.genre,
              'rating': self.rating
         }

# clear database
'''
with app.app_context():
    Film.query.delete()
    db.session.commit()
'''

with app.app_context():
    db.create_all()
    if Film.query.count() == 0:
        db.session.add_all([
            Film("Spirited Away", "Animation", "PG"),
            Film("Midsommar", "Horror", "R"),
            Film("My Cousin Vinny", "Comedy", "R"),
            Film("Invasion of the Body Snatchers", "Sci-Fi", "PG")
        ])
        db.session.commit()

# data dictionary for JSON
data = {
     "id": Film.id,
     "title": Film.title,
     "genre": Film.genre,
     "rating": Film.rating 
          }

#home page
@app.route('/')
def index():
    return render_template('index.html')

#about page
@app.route('/about')
def about():
    return render_template('about.html')

# fortune teller page
@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    user = request.form.get('user')
    color = request.form.get('color')
    number = request.form.get('number')

    if request.method == 'POST':
        if color == "red":
            if number == "1":
                return render_template('fortune.html', fortune=f"{user}, a slotted spoon doesn't hold much soup.")
            if number == "2":
                return render_template('fortune.html', fortune=f"{user}, the ball is in your court.")
            if number == "3":
                return render_template('fortune.html', fortune=f"{user}, every cloud has a silver lining.")
            if number == "4":
                return render_template('fortune.html', fortune=f"{user}, don't put all your eggs in one basket.")
            
        if color == "yellow":
            if number == "1":
                return render_template('fortune.html', fortune=f"{user}, you can't have your cake and eat it too.")
            if number == "2":
                return render_template('fortune.html', fortune=f"{user}, the early bird catches the worm.")
            if number == "3":
                return render_template('fortune.html', fortune=f"{user}, too many cooks spoil the broth.")
            if number == "4":
                return render_template('fortune.html', fortune=f"{user}, Rome wasn't built in a day.")
            
        if color == "blue":
            if number == "1":
                    return render_template('fortune.html', fortune=f"{user}, a stitch in time saves nine.")
            if number == "2":
                    return render_template('fortune.html', fortune=f"{user}, if the shoe fits, wear it.")
            if number == "3":
                    return render_template('fortune.html', fortune=f"{user}, don't judge a book by its cover.")
            if number == "4":
                    return render_template('fortune.html', fortune=f"{user}, the squeaky wheel gets the grease.")
            
        if color == "green":
            if number == "1":
                    return render_template('fortune.html', fortune=f"{user}, throw caution to the wind.")
            if number == "2":
                    return render_template('fortune.html', fortune=f"{user}, a watched pot never boils.")
            if number == "3":
                    return render_template('fortune.html', fortune=f"{user}, don't bite off more than you can chew.")
            if number == "4":
                    return render_template('fortune.html', fortune=f"{user}, don't count your chickens before they hatch.")
    return render_template('fortune.html')

# films page
@app.route('/films')
def show_films():
    all_films = Film.query.all()
    return render_template('films.html', films=all_films)

# film detail page
@app.route('/films/<int:film_id>')
def film_detail(film_id):
    film = Film.query.get_or_404(film_id)
    return render_template('film_detail.html', film=film)

# return JSON data
@app.route('/api/films')
def api_films():
     return jsonify([film.serialize for film in Film.query.all()])

@app.post('/api/add_film')
def add_film():
    data = request.get_json()
    try:
        film = Film(title=data['title'], genre=data['genre'], rating=data['rating'])
        db.session.add(film)
        db.session.commit()
        return jsonify({"status": "success"})
    except Exception:
        return app.response_class(response={"status": "failure"},
                                  status=500,
                                  mimetype='application/json')

# run app    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)