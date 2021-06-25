from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
#redirect and url_for are used for redirecting user.
#redner_template is used to import html templates

app = Flask(__name__)
admin_enable = False #Enable to access /admin.

@app.route("/") #When this is URL, landing() executed.
def landing():
    return render_template("landing.html")
@app.route("/home") #When this is URL, home() executed.
def home():
    return render_template("home.html")

@app.route("/week1") #When this is URL, week1() executed.
def week1():
    return render_template("week1.html")

@app.route("/week2") #When this is URL, week2() executed.
def week2():
    return render_template("week2.html")

@app.route("/admin") #When this is URL, admin() executed.
def admin():
    if admin_enable == False:
        return(redirect(url_for("error")))
    else:
        data = pd.read_csv("database.csv")
        print("Latest Entries: \n")
        print(data.head())
        return render_template("admin.html")

@app.route("/error") #When this is URL, error() executed.
def error():
    return render_template("error.html")

@app.route("/register", methods=["POST", "GET"]) #When this is URL, tryy() executed. We specify using both GET and POST.
def register():
    # If first time (no input yet, goes to else condition and uses blank form using GET i.e. blank form.) Else executes code under if.
    if request.method == 'POST':
        name = request.form["Name"]
        num = request.form["Num"]
        year = request.form["Year"]
        data = pd.DataFrame([[name,num,year]], columns=['Name', 'Contact Number', 'Year'])
        data.to_csv('database.csv', mode='a', index=False, header=False) #mode='a' signifies adding to existing csv
        return(redirect(url_for("registered")))
    else:
        return render_template("register.html")

@app.route("/registered") #When this is URL, registered() executed.
def registered():
    return render_template("registered.html")

if __name__ == "__main__":
    app.run(debug='True') #When debug = True, we need not run code everytime to update server.