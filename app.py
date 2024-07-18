from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/madlib', methods=['GET', 'POST'])
def madlib():
    if request.method=='POST':
        return f'Thanks for submitting the form {request.form["fname"]}!'
    return render_template('madlib.html', signup=url_for('signup'))


@app.route('/complete')
def complete():
    return 'Goodbye, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)