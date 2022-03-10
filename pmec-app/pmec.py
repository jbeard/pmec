import os

from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "investor.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Investor(db.Model):
    firstname = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<FirstName: {}>".format(self.firstname)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        investor = Investor(firstname=request.form.get("firstname"))
        db.session.add(investor)
        db.session.commit()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

