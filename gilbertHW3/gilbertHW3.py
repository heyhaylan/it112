from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

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



    
if __name__ == "__main__":
    app.run(debug=True)