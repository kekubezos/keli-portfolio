from flask import Flask, render_template, request, redirect

import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<page_name>")
def my_components(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        text_file = database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open('database.csv', mode='a', newline="") as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        csv_file = csv.writer(database_csv, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, message])


@app.route("/submit_form", methods=['POST'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thank-you.html")

        except:
            return "Did not save to database"

    else:
        return "Something went wrong. Try again!"
