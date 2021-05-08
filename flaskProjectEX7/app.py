from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')  # defines which func will run when uploading the ROOT page
def hello_world():
    return redirect(url_for('welcome_to'))


@app.route('/about')  # defines which func will run when opening the ABOUT page
def hello_about():
    already_seen_about = True
    if already_seen_about:

        return redirect('/')  # redirect func redirect you to the page that you want by some
    else:
        return 'Welcome to the ABOUT page'


@app.route('/more')
def welcome_to():
    return 'Welcome to the ROOT page by url_for by more'


if __name__ == '__main__':
    app.run(debug=True)
