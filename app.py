from flask import Flask, render_template, url_for, request
from datetime import date, datetime
from calendaria import round_vals_from_date, rof, daynbr


# Formats
date_title_fmt = "%d of %B, %Y"

# Create the app
app = Flask(__name__)

@app.route('/')
def index():
    indate = date.today()
    vals = round_vals_from_date(indate)
    date_title = indate.strftime(date_title_fmt)
    rof_ = rof(indate)
    rof_day = daynbr(indate)
    return render_template('index.html', 
                           date_title=date_title,
                           vals=vals,
                           rof_=rof_,
                           rof_day=rof_day)

@app.route('/', methods=['POST'])
def date_form():
    input_date = request.form['inputdate']
    try:
        indatetime = datetime.strptime(input_date, "%d/%m/%Y")
        indate = date(indatetime.year, indatetime.month, indatetime.day)
    except:
        indate = date.today()
    finally:
        date_title = indate.strftime(date_title_fmt)
        vals = round_vals_from_date(indate)
        rof_ = rof(indate)
        rof_day = daynbr(indate)
    return render_template('index.html', 
                           date_title=date_title,
                           vals=vals,
                           rof_=rof_,
                           rof_day=rof_day)

if __name__ == "__main__":
    app.run(debug=True)