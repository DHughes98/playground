from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Level_1')
@app.route ('/Level_1/<int:num>')
@app.route ('/Level_1/<int:num>/<color>')
def Level_1(num = 3, color = "blue"):
    print("test")
    return render_template("box.html",n  = num, color = color )




if __name__ == "__main__":
    app.run(debug=True)