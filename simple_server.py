from flask import Flask,render_template,url_for,redirect

app = Flask(__name__)

# ルーティング
@app.route('/')
def index_func():
  return redirect(url_for('next_func')) #url_for('method_name')

@app.route("/next")
def next_func():
  return render_template('index.html', message="花子さん")


@app.route("/hello")
def hello_world():
    return "Hello world"

@app.route("/user/<username>")
def show_user_profile(username):
    return "UserName: " + str(username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post" + str(post_id)

if __name__ == "__main__":
    app.run(port=8000, debug=True)