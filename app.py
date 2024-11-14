from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def about():
    return render_template('about.html')

@app.route('/')
def services():
    return render_template('services.html')


@app.route('/')
def contact():
    return render_template('contact.html')

@app.route('/')
def pagelogin():
    return render_template('page-login.html')

@app.route('/')
def pagesignup():
    return render_template('page-signup.html')



if __name__=='__main__':
    app.run(debug=True)