from flask import Flask,render_template,send_from_directory
from data_pm import *
from datetime import timedelta,datetime

app = Flask(__name__)

app.register_blueprint(showdatapm)
app.secret_key = ""
app.permanent_session_lifetime = timedelta(hours=1)

start_time = datetime.now()

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

