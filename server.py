from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set secret key for security

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # print(request.form)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    # print('Showing the User Info From the form')
    # print(request.form)
    return render_template('show.html')

# Error message for 404
@app.errorhandler(404)
def page_not_found(e):
    return f'Sorry! No response. Try again.'

# Ensure file is run directly and not from different
# module, and run localhost on port 5001 for mac
if __name__=="__main__":
    app.run(host='localhost', port=5001, debug=True)
