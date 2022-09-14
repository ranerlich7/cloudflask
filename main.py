from flask import Flask, render_template

import auth
app = Flask(__name__)

app.register_blueprint(auth.bp)


@app.route("/")
def hello_world():
   return render_template("home.html")
 
if __name__ == '__main__':
   app.run(debug=True)