from flask import Flask, render_template
app = Flask(__name__)
@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
      {'name' : 'Michael', 'age' : 35},
      {'name' : 'John', 'age' : 30 },
      {'name' : 'Mark', 'age' : 25},
      {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)
@app.route('/')
def hello_world():
  return render_template("index.html", phrase="hello", times=5)
  # print("in the hello function")
  # return render_template('index.html')
@app.route('/success')
def success():
  return "success"
@app.route('/hello/<name>')
def hello(name):
  print(name)
  return "Hello, " + name
@app.route('/users/<username>/<id>')
def shwo_user_profile(username, id):
  print(username)
  print(id)
  return "username:" + username + ", id: "+ id

if __name__ == "__main__":
  app.run(debug=True)