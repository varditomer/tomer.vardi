from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


# defines which func will run when uploading the ROOT page
@app.route('/main')
@app.route('/home')
@app.route('/')
def index():
    name = 'TomEr'
    title = 'Tomer Online CV'
    return render_template('cv.html',
                           curr_user={'firstname': name, 'lastname': 'vardi'},
                           title=title)


@app.route('/header')
def header():
    return render_template('header.html')


@app.route('/customers')
def customers():
    return render_template('customers.html')


@app.route('/assignment8')
def hello_ass8():
    name = 'TomEr'
    title = 'Hobbies'
    return render_template('assignment8.html',
                           curr_user={'firstname': name, 'lastname': 'vardi'},
                           title=title,
                           hobbies=['surf','poker','parties','pycharm :-)'])


@app.route('/usersList')
def users_list():
    return render_template('usersList.html')


@app.route('/facebook')
def facebook_link():
    return redirect('https://www.facebook.com/tomerv/')


@app.route('/linkedin')
def linkedin_link():
    return redirect('https://www.linkedin.com/in/tomer-vardi/')


@app.route('/awesome_stylesheet')
def awesome():
    return redirect('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css')


if __name__ == '__main__':
    app.run(debug=True)
