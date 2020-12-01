from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def check_board1():
  return render_template("index.html", row = 8, column = 8, new_line = "\n")
@app.route('/<int:column>')
def check_board2(column):
  return render_template("index.html", row = 8, column = column, new_line = "\n" )
@app.route('/<int:column>/<int:row>')
def check_board3(column, row):
  return render_template("index.html", row = row, column = column, new_line = "\n")
@app.route('/<int:column>/<int:row>/<color1>/<color2>')
def check_board4(column, row, color1, color2):
  return render_template("index.html", row = row, column = column, new_line = "\n", color1 = color1, color2 = color2)

if __name__ == "__main__":
  app.run(debug=True)