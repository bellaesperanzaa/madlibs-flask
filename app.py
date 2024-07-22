from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/madlib', methods=['GET', 'POST'])
def madlib():
    if request.method=='POST':
        adjective1 = request.form['adjective1']
        noun1 = request.form['noun1']
        verb1= request.form['verb1']
        adverb1 = request.form['adverb1']
        adjective2  = request.form['adjective2']
        noun2  = request.form['noun2']
        verb2  = request.form['verb2']
        place  = request.form['place']
        pluralnoun  = request.form['plural noun']
        emotion  = request.form['emotion']
        return render_template('complete.html', adjective1=adjective1, noun1=noun1, verb1=verb1, adverb1=adverb1, adjective2=adjective2, noun2=noun2, verb2=verb2, place=place, pluralnoun=pluralnoun, emotion=emotion)
    return render_template('madlib.html', madlib=url_for('madlib'))


@app.route('/complete')
def complete():
    return 'Goodbye, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)