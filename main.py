from flask import Flask, render_template
import requests

app = Flask(__name__)


#enlace del api
url_blog = "https://api.npoint.io/27ac7d8df827e3646309"
response = requests.get(url_blog)
all_post = response.json()

@app.route('/')
def blog():
    return render_template("index.html",posts = all_post)

@app.route('/post/<int:num>')
def post(num):
    for post in all_post:
        if num == post["id"]:
            return render_template("post.html",post=post)

if __name__ == "__main__":
    app.run(debug=True)
