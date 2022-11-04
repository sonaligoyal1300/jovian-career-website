from flask import Flask, render_template

app = Flask(__name__)

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
def hello_world():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug="True")
