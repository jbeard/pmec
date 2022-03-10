import os

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

# this is the working directory of the project; not using more sophisticated filesystem management
project_dir = os.path.dirname(os.path.abspath(__file__))
# investor database name defined as hardcoded 'investor.db' here
database_file = "sqlite:///{}".format(os.path.join(project_dir, "investor.db"))

# this defines that uploads are made in a subdirectory of the project working directory
UPLOAD_FOLDER = project_dir + "/upload"
# limit filetypes to acceptable formats as a limited error prevention hedge
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

class Investor(db.Model):
#    hash = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    firstname = db.Column(db.String(80), unique=False, nullable=False, primary_key=True)
    lastname = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    dob = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    phone = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    address = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    # should we have city here too?
    state = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    zip = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    investorfile = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)

    def __repr__(self):
        return "<FirstName: {}>".format(self.firstname)+"<LastName: {}>".format(self.lastname)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def home():
    investors = None
    if request.form:
        try:
            investor = Investor( firstname=request.form.get("firstname"), lastname=request.form.get("lastname"), dob=request.form.get("dob"), phone=request.form.get("phone"), address=request.form.get("address"), state=request.form.get("state"), zip=request.form.get("zip"), investorfile="none" )
            db.session.add(investor)
            db.session.commit()
        except Exception as e:
            print("ERROR: Failed to add Investor")
            print(e)
    investors = Investor.query.all()
    return render_template("index.html", investors=investors)

@app.route("/update", methods=["POST"])
def update():
    try:
        newfirstname = request.form.get("newfirstname")
        oldfirstname = request.form.get("oldfirstname")
        investor = Investor.query.filter_by(firstname=oldfirstname).first()
        investor.firstname = newfirstname
        db.session.commit()
    except Exception as e:
        print("ERROR: Failed to update Investor")
        print(e)
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    firstname = request.form.get("firstname")
    investor = Investor.query.filter_by(firstname=firstname).first()
    db.session.delete(investor)
    db.session.commit()
    return redirect("/")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            try:
                oldfirstname = request.form.get("oldfirstname")
                investor = Investor.query.filter_by(firstname=oldfirstname).first()
                investor.investorfile = filename
                db.session.commit()
            except Exception as e:
                print("ERROR: Failed to update Investor's uploaded filename")
                print(e)
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

