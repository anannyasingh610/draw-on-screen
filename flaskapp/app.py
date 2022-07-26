from flask import Flask, render_template
import painter as p

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():

  return p.paint()

if __name__ == '__main__':
  app.run(debug=True)
