from flask import Flask, render_template, redirect, url_for, request

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


@app.route("/")
def world():
  return render_template('login.html')
  # return render_template('home.html', jobs=JOBS)


@app.route("/test")
def test():
  # return render_template('login.html')
  return render_template('test.html', jobs=JOBS)


@app.route("/home")
def hello_world():
  return render_template('home.html', jobs=JOBS)
  # return render_template('home.html')


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug="True")
