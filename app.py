from flask import Flask, request,  render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello guys. This is index page...'


@app.route('/home')
def home():
    return 'This is home page...'


@app.route('/profile/')
@app.route('/profile/<username>')
def profile(username=None):
    return render_template("profile.html", username=username)
    # return 'Hello %s' % username + '. This is profile page...'


@app.route('/show/<int:uid>')
def show(uid):
    return 'User ID : %s' % uid


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        return 'You are using POST Method'
    else:
        return 'You are using GET Method'


@app.route('/tasks', methods=['GET'])
def tasks():
    tasklist = ['One', 'Two', 'Three', 'Four']
    return render_template("tasks.html", tasklist=tasklist)


if __name__ == '__main__':
    app.run(debug=True)
