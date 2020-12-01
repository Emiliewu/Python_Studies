from flask import Flask
app = Flask(__name__)
from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response, try again!"
@app.route('/')
def hello_world():
  return "Hello World!"
@app.route('/dojo')
def dojo():
  return "Dojo!"
@app.route('/say/<name>')
def say_name(name):
  return "Hi {}!".format(name.capitalize())
@app.route('/repeat/<int:repeat_num>/<repeat_word>')
def repeat_info(repeat_num, repeat_word):
  return f"{repeat_word} " * repeat_num

if __name__ == "__main__":
  app.run(debug = True)