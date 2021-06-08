from flask import Flask, Blueprint, render_template, session, redirect, request
import mysql.connector

# assignment10 blueprint definition
assignment10 = Blueprint(
    'assignment10',
    __name__,
    static_folder='static',
    static_url_path='/pages/assignment10',
    template_folder='templates'
)


# assignment10 routes
@assignment10.route('/assignment10')
def index():
    return render_template('assignment10.html')


@assignment10.route('/usersListAs10')
def users_list():
    return render_template('usersListAs10.html')


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
# --------------SELECT-------------------- #
# ------------------------------------- #
@assignment10.route('/users')
def users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


# ------------------------------------- #
# --------------END SELECT------------- #
# ------------------------------------- #

# ------------------------------------- #
# --------------INSERT----------------- #
# ------------------------------------- #
@assignment10.route('/insert_user', methods=['GET', 'POST'])
def insert_users():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        query = "INSERT INTO users(first_name, last_name , email) VALUES ('%s', '%s', '%s')" \
                % (first_name, last_name, email)
        interact_db(query=query, query_type='commit')
        return redirect('/users')
    return render_template('assignment10.html')


# ------------------------------------- #
# --------------END INSERT------------- #
# ------------------------------------- #

# ------------------------------------- #
# --------------DELETE----------------- #
# ------------------------------------- #
@assignment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form['id']
        query = "delete from users where id ='%s';" % user_id
        interact_db(query, query_type='commit')
        return redirect('/users')
    return redirect('/users')


# ------------------------------------- #
# --------------END DELETE------------- #
# ------------------------------------- #

# ------------------------------------- #
# --------------UPDATE----------------- #
# ------------------------------------- #
@assignment10.route('/update_user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        user_id = request.form['id']
        if request.form['firstname']:
            new_first_name = request.form['firstname']
            query = "update users set first_name = '%s' where id ='%s';" % (new_first_name, user_id)
            interact_db(query, query_type='commit')
        if request.form['lastname']:
            new_last_name = request.form['lastname']
            query = "update users set last_name = '%s' where id ='%s';" % (new_last_name, user_id)
            interact_db(query, query_type='commit')
        if request.form['email']:
            new_email = request.form['email']
            query = "update users set email = '%s' where id ='%s';" % (new_email, user_id)
            interact_db(query, query_type='commit')
        return redirect('/users')
    return redirect('/users')
# ------------------------------------- #
# --------------END UPDATE------------- #
# ------------------------------------- #
