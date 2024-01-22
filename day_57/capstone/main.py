from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

@app.route('/')
def home():
    blog_posts = requests.get(blog_url).json()
    return render_template("index.html", posts=blog_posts)

@app.route('/blog/<blog_id>')
def get_blog(blog_id):
    post = Post(requests.get(blog_url).json()[int(blog_id)-1])
    return render_template("post.html", post=post)
    
if __name__ == "__main__":
    app.run(debug=True)
