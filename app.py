from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)
app.secret_key = "secret key"

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Karnatka',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Gurugram',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 3,
  'title': 'Front-end Engineer',
  'location': 'Noida',
  'salary': 'Rs. 12,00,000'
}, {
  'id': 4,
  'title': 'Back-end Engineer',
  'location': 'Noida',
  'salary': 'Rs. 12,00,000'
}]


@app.route("/", methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    connection = sqlite3.connect('user_data.db')
    cursor = connection.cursor()
    name = request.form['name']
    password = request.form['password']
    print(name, password)
    query = "SELECT name,password from users where name= '" + name + "' and password= '" + password + "' "
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) == 0:
      return render_template("invalid.html")
    else:
      return render_template("home.html", jobs=JOBS)

  return render_template("login.html")
  # return render_template("home.html", jobs=JOBS)


# return render_template('login.html')
# # return render_template('home.html', jobs=JOBS)
@app.route("/registration", methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    connection = sqlite3.connect('user_data.db')
    cursor = connection.cursor()
    name = request.form['name']
    password = request.form['password']
    print(name, password)
    query = "INSERT INTO users (name, password) VALUES ('" + name + "' ,'" + password + "') "
    cursor.execute(query)
    connection.commit()
    connection.close()
    return render_template('login.html')

    # result = cursor.fetchall()
    # if len(result) == 0:
    #   return render_template("invalid.html")
    # else:
    #   return render_template("home.html", jobs=JOBS)

  return render_template("registration.html")


@app.route("/invalid")
def test():
  # return render_template('login.html')
  return render_template('invalid.html', jobs=JOBS)


@app.route("/home")
def hello_world():
  return render_template('home.html', jobs=JOBS)
  # return render_template('home.html')


# @app.route("/registration")
# def register():
#   return render_template('registration.html')
#   # return render_template('home.html')

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug="True")
