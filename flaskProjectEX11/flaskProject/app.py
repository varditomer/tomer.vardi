from flask import Flask, render_template, redirect, url_for, request, session, Blueprint, jsonify
import mysql.connector

# App setup
app = Flask(__name__)
app.secret_key = '123'

# Pages
# Assignment10
from pages.assignment10.assignment10 import assignment10

app.register_blueprint(assignment10)


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
                           hobbies=['surf', 'poker', 'parties', 'pycharm :-)'])


@app.route('/assignment9', methods=['POST', 'PUT', 'DELETE', 'GET'])
def hello_ass9():
    return render_template('assignment9.html', parameters=request.args)


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


@app.route('/search')
def searchform():
    users = [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ]
    if 'searchinput' in request.args:
        search = request.args['searchinput']
    else:
        search = ""
    if search == "":
        return render_template('assignment9.html', search=users)
    flag = False
    for user in users:
        if user['first_name'] == search or user['email'] == search:
            flag = True
            return render_template('assignment9.html', searchfound=user)
    if not flag:
        return render_template('assignment9.html', notfound="Item not found!")


@app.route('/register', methods=['POST'])
def registerform():
    if 'username' in request.form:
        user_name = request.form['username']
        user_pass = request.form['password']
        user_email = request.form['email']
        user_nickname = request.form['nickname']
    else:
        user_name, user_pass, user_email, user_nickname = '', '', '', ''
    session['username'] = user_name
    session['password'] = user_pass
    session['email'] = user_email
    session['nickname'] = user_nickname
    return render_template('assignment9.html', user_name=user_name, user_pass=user_pass, user_email=user_email,
                           user_nickname=user_nickname)


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        session.pop('password', None)
        session.pop('email', None)
        session.pop('nickname', None)
        return render_template('assignment9.html')


# ------------------------------------- #
# ---------DATABASE CONNECTION--------- #
# ------------------------------------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='assignment10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # use for INSERT UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if succeed
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# ------------------------------------- #
# -----END DATABASE CONNECTION--------- #
# ------------------------------------- #

# ------------------------------------- #
# -----Assignment 11------------------- #
# ------------------------------------- #
@app.route('/assignment11/users/selected', defaults={'SOME_USER_ID': 26})
@app.route('/assignment11/users/selected/<int:SOME_USER_ID>')
def profile_func(SOME_USER_ID):
    if SOME_USER_ID == 26:
        query = "SELECT * FROM users WHERE id=26;"
        query_result = interact_db(query=query, query_type='fetch')
        response = query_result[0]
        response = jsonify(response)
        return response
    else:
        query = "SELECT * FROM users WHERE id='%s';" % SOME_USER_ID
        query_result = interact_db(query=query, query_type='fetch')
        response = {}
        if len(query_result) != 0:
            response = query_result[0]
        else:
            return "This user doesn't exist "
        response = jsonify(response)
    return response


@app.route('/assignment11/users')
def returnusersjsonify():
    if request.method == 'GET':
        query = "select * from users"
        query_result = interact_db(query=query, query_type='fetch')
        data = list(map(lambda row: row._asdict(), query_result))
        data = jsonify(data)
    return data


# ------------------------------------- #
# -----Assignment 11 END--------------- #
# ------------------------------------- #


if __name__ == '__main__':
    app.run(debug=True)
