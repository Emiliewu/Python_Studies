from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<int:repeat_num>/<block_color>')
def display_blocks(repeat_num, block_color):
  return render_template("index.html", block_color = block_color, times = repeat_num )

if __name__ == "__main__":
  app.run(debug=True)