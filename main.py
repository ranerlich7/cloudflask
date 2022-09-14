from flask import Flask, render_template

app = Flask(__name__)

# import auth
# app.register_blueprint(auth.bp)


@app.route("/")
def hello_world():
   return render_template("home.html")
 
if __name__ == '__main__':
   app.run(debug=True)